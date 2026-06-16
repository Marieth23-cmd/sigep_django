from django.db import models


class Escola(models.Model):
    ESTADO_CHOICES = [
        ('ATIVADA', 'Ativada'),
        ('DESATIVADA', 'Desativada'),
        ('EXCLUIDA', 'Excluída'),
    ]

    id_escola = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    nif = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=150, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    logo = models.URLField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ATIVADA'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'escolas'
        verbose_name_plural = 'Escolas'

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    CARGO_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('FINANCEIRO', 'Financeiro'),
        ('RECEPCAO', 'Recepção'),
    ]

    ESTADO_CHOICES = [
        ('ATIVADO', 'Ativado'),
        ('DESATIVADO', 'Desativado'),
    ]

    id_usuario = models.AutoField(primary_key=True)
    id_escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    senha = models.CharField(max_length=255)
    cargo = models.CharField(
        max_length=30,
        choices=CARGO_CHOICES
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ATIVADO'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'
        unique_together = ('id_escola', 'email')
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    id_escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    propina_mensal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'cursos'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome
class Turma(models.Model):
    PERIODO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite'),
    ]

    id_turma = models.AutoField(primary_key=True)
    id_escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES)
    sala = models.IntegerField(null=True, blank=True)        
    ano_letivo = models.IntegerField(null=True, blank=True)  

    class Meta:
        db_table = 'turmas'
        verbose_name_plural = 'Turmas'
        unique_together = [['nome', 'id_curso', 'periodo']]  # ✅ impede duplicatas

    def __str__(self):
        return f"{self.nome} - {self.periodo}"


class Bolsa(models.Model):
    ESTADO_CHOICES = [
        ('ATIVA', 'Ativa'),
        ('INATIVA', 'Inativa'),
    ]

    id_bolsa = models.AutoField(primary_key=True)
    id_escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipo_bolsa = models.CharField(max_length=50, null=True, blank=True)
    percentual_desconto = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ATIVA'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bolsas'
        verbose_name_plural = 'Bolsas'

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Ativo'),
        ('INACTIVO', 'Inativo'),
        ('TRANSFERIDO', 'Transferido'),
    ]

    id_aluno = models.AutoField(primary_key=True)
    id_escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    id_bolsa = models.ForeignKey(Bolsa, on_delete=models.SET_NULL, null=True, blank=True)
    numero_aluno = models.IntegerField()
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=20, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone_encarregado = models.CharField(max_length=30, null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ACTIVO'
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'alunos'
        unique_together = ('numero_aluno', 'id_turma')
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome


class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    mes = models.IntegerField()
    ano = models.IntegerField()
    valor_propina = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(max_length=30, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pagamentos'
        unique_together = ('id_aluno', 'mes', 'ano')
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return f"Pagamento {self.id_aluno} - {self.mes}/{self.ano}"


class Auditoria(models.Model):
    id_auditoria = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acao = models.CharField(max_length=100, null=True, blank=True)
    tabela_afetada = models.CharField(max_length=100, null=True, blank=True)
    data_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'auditoria'
        verbose_name_plural = 'Auditorias'

    def __str__(self):
        return f"Auditoria - {self.acao}"


class ConfiguracaoEscola(models.Model):
    id_config = models.AutoField(primary_key=True)
    id_escola = models.OneToOneField(Escola, on_delete=models.CASCADE, unique=True)
    moeda = models.CharField(max_length=10, default='AOA')
    permitir_atraso = models.BooleanField(default=True)
    dias_tolerancia = models.IntegerField(default=5)

    class Meta:
        db_table = 'configuracoes_escola'
        verbose_name_plural = 'Configurações de Escola'

    def __str__(self):
        return f"Config - {self.id_escola.nome}"
