from decimal import Decimal

from rest_framework import serializers
from .models import (
    Escola,
    Usuario,
    Curso,
    Turma,
    Bolsa,
    Aluno,
    Pagamento,
    Auditoria,
    ConfiguracaoEscola,
)


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    escola_nome = serializers.CharField(source='id_escola.nome', read_only=True)

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'id_escola', 'escola_nome', 'nome', 'email', 'cargo', 'estado', 'data_criacao']


class CursoSerializer(serializers.ModelSerializer):
    escola_nome = serializers.CharField(source='id_escola.nome', read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'


from rest_framework.validators import UniqueTogetherValidator

class TurmaSerializer(serializers.ModelSerializer):
    escola_nome = serializers.CharField(source='id_escola.nome', read_only=True)
    curso_nome = serializers.CharField(source='id_curso.nome', read_only=True)

    class Meta:
        model = Turma
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Turma.objects.all(),
                fields=['id_curso', 'nome'],
                message='Já existe uma turma com esse nome para este curso.'
            )
        ]


class BolsaSerializer(serializers.ModelSerializer):
    escola_nome = serializers.CharField(source='id_escola.nome', read_only=True)

    class Meta:
        model = Bolsa
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    escola_nome = serializers.CharField(source='id_escola.nome', read_only=True)
    turma_nome = serializers.CharField(source='id_turma.nome', read_only=True)
    sala = serializers.IntegerField(source='id_turma.sala', read_only=True)
    periodo = serializers.CharField(source='id_turma.periodo', read_only=True)
    propina_mensal = serializers.DecimalField(source='id_turma.id_curso.propina_mensal', max_digits=10, decimal_places=2, read_only=True)
    curso_nome = serializers.CharField(source='id_turma.id_curso.nome', read_only=True)  # ✅ novo
    bolsa_nome = serializers.CharField(source='id_bolsa.nome', read_only=True, allow_null=True)
    bolsa_desconto = serializers.DecimalField(source='id_bolsa.percentual_desconto', max_digits=5, decimal_places=2, read_only=True, allow_null=True)

    class Meta:
        model = Aluno
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source='id_aluno.nome', read_only=True)
    aluno_numero = serializers.IntegerField(source='id_aluno.numero_aluno', read_only=True)
    turma_nome = serializers.CharField(source='id_aluno.id_turma.nome', read_only=True)
    sala = serializers.IntegerField(source='id_aluno.id_turma.sala', read_only=True)
    periodo = serializers.CharField(source='id_aluno.id_turma.periodo', read_only=True)
    curso_nome = serializers.CharField(source='id_aluno.id_turma.id_curso.nome', read_only=True)

    class Meta:
        model = Pagamento
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Pagamento.objects.all(),
                fields=['id_aluno', 'mes', 'ano'],
                message='Este aluno ja tem pagamento registado para este mes e ano.'
            )
        ]

    def _valor_devido(self, aluno):
        propina = aluno.id_turma.id_curso.propina_mensal
        if aluno.id_bolsa_id and aluno.id_bolsa:
            desconto = aluno.id_bolsa.percentual_desconto or Decimal('0')
            propina = propina * (Decimal('100') - desconto) / Decimal('100')
        return propina.quantize(Decimal('0.01'))

    def validate_mes(self, value):
        if value < 1 or value > 12:
            raise serializers.ValidationError('O mes deve estar entre 1 e 12.')
        return value

    def validate(self, attrs):
        attrs = super().validate(attrs)
        aluno = attrs.get('id_aluno') or getattr(self.instance, 'id_aluno', None)
        if not aluno:
            return attrs

        valor_devido = self._valor_devido(aluno)
        valor_propina = attrs.get('valor_propina')
        valor_pago = attrs.get('valor_pago')

        if valor_propina is not None and valor_propina != valor_devido:
            raise serializers.ValidationError({
                'valor_propina': f'O valor da propina deste aluno e {valor_devido} Kz.'
            })

        if valor_pago is not None and valor_pago != valor_devido:
            raise serializers.ValidationError({
                'valor_pago': f'O aluno deve pagar exatamente {valor_devido} Kz para este mes.'
            })

        attrs['valor_propina'] = valor_devido
        attrs['valor_pago'] = valor_devido
        return attrs


class AuditoriaSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='id_usuario.nome', read_only=True)

    class Meta:
        model = Auditoria
        fields = '__all__'


class ConfiguracaoEscolaSerializer(serializers.ModelSerializer):
    escola_nome = serializers.CharField(source='id_escola.nome', read_only=True)

    class Meta:
        model = ConfiguracaoEscola
        fields = '__all__'
