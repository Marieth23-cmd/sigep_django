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
    bolsa_nome = serializers.CharField(source='id_bolsa.nome', read_only=True, allow_null=True)

    class Meta:
        model = Aluno
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source='id_aluno.nome', read_only=True)

    class Meta:
        model = Pagamento
        fields = '__all__'


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
