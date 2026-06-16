from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
from .serializers import (
    EscolaSerializer,
    UsuarioSerializer,
    CursoSerializer,
    TurmaSerializer,
    BolsaSerializer,
    AlunoSerializer,
    PagamentoSerializer,
    AuditoriaSerializer,
    ConfiguracaoEscolaSerializer,
)


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

    @action(detail=True, methods=['get'])
    def usuarios(self, request, pk=None):
        """Retorna todos os usuários de uma escola"""
        escola = self.get_object()
        usuarios = Usuario.objects.filter(id_escola=escola)
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def alunos(self, request, pk=None):
        """Retorna todos os alunos de uma escola"""
        escola = self.get_object()
        alunos = Aluno.objects.filter(id_escola=escola)
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def cursos(self, request, pk=None):
        """Retorna todos os cursos de uma escola"""
        escola = self.get_object()
        cursos = Curso.objects.filter(id_escola=escola)
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def turmas(self, request, pk=None):
        """Retorna todas as turmas de uma escola"""
        escola = self.get_object()
        turmas = Turma.objects.filter(id_escola=escola)
        serializer = TurmaSerializer(turmas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def bolsas(self, request, pk=None):
        """Retorna todas as bolsas de uma escola"""
        escola = self.get_object()
        bolsas = Bolsa.objects.filter(id_escola=escola)
        serializer = BolsaSerializer(bolsas, many=True)
        return Response(serializer.data)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['get'])
    def por_escola(self, request):
        """Retorna usuários de uma escola específica"""
        escola_id = request.query_params.get('escola_id')
        if not escola_id:
            return Response({'erro': 'escola_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        usuarios = Usuario.objects.filter(id_escola=escola_id)
        serializer = self.get_serializer(usuarios, many=True)
        return Response(serializer.data)


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=False, methods=['get'])
    def por_escola(self, request):
        """Retorna cursos de uma escola específica"""
        escola_id = request.query_params.get('escola_id')
        if not escola_id:
            return Response({'erro': 'escola_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        cursos = Curso.objects.filter(id_escola=escola_id)
        serializer = self.get_serializer(cursos, many=True)
        return Response(serializer.data)


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

    @action(detail=False, methods=['get'])
    def por_escola(self, request):
        """Retorna turmas de uma escola específica"""
        escola_id = request.query_params.get('escola_id')
        if not escola_id:
            return Response({'erro': 'escola_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        turmas = Turma.objects.filter(id_escola=escola_id)
        serializer = self.get_serializer(turmas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def alunos(self, request, pk=None):
        """Retorna todos os alunos de uma turma"""
        turma = self.get_object()
        alunos = Aluno.objects.filter(id_turma=turma)
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)


class BolsaViewSet(viewsets.ModelViewSet):
    queryset = Bolsa.objects.all()
    serializer_class = BolsaSerializer

    @action(detail=False, methods=['get'])
    def por_escola(self, request):
        """Retorna bolsas de uma escola específica"""
        escola_id = request.query_params.get('escola_id')
        if not escola_id:
            return Response({'erro': 'escola_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        bolsas = Bolsa.objects.filter(id_escola=escola_id)
        serializer = self.get_serializer(bolsas, many=True)
        return Response(serializer.data)


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=False, methods=['get'])
    def por_escola(self, request):
        """Retorna alunos de uma escola específica"""
        escola_id = request.query_params.get('escola_id')
        if not escola_id:
            return Response({'erro': 'escola_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        alunos = Aluno.objects.filter(id_escola=escola_id)
        serializer = self.get_serializer(alunos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def por_turma(self, request):
        """Retorna alunos de uma turma específica"""
        turma_id = request.query_params.get('turma_id')
        if not turma_id:
            return Response({'erro': 'turma_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        alunos = Aluno.objects.filter(id_turma=turma_id)
        serializer = self.get_serializer(alunos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def pagamentos(self, request, pk=None):
        """Retorna todos os pagamentos de um aluno"""
        aluno = self.get_object()
        pagamentos = Pagamento.objects.filter(id_aluno=aluno)
        serializer = PagamentoSerializer(pagamentos, many=True)
        return Response(serializer.data)


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    @action(detail=False, methods=['get'])
    def por_aluno(self, request):
        """Retorna pagamentos de um aluno específico"""
        aluno_id = request.query_params.get('aluno_id')
        if not aluno_id:
            return Response({'erro': 'aluno_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        pagamentos = Pagamento.objects.filter(id_aluno=aluno_id)
        serializer = self.get_serializer(pagamentos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def por_mes_ano(self, request):
        """Retorna pagamentos de um mês e ano específicos"""
        mes = request.query_params.get('mes')
        ano = request.query_params.get('ano')
        
        if not mes or not ano:
            return Response({'erro': 'mes e ano são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
        
        pagamentos = Pagamento.objects.filter(mes=mes, ano=ano)
        serializer = self.get_serializer(pagamentos, many=True)
        return Response(serializer.data)


class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer

    @action(detail=False, methods=['get'])
    def por_usuario(self, request):
        """Retorna ações de auditoria de um usuário específico"""
        usuario_id = request.query_params.get('usuario_id')
        if not usuario_id:
            return Response({'erro': 'usuario_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        auditorias = Auditoria.objects.filter(id_usuario=usuario_id)
        serializer = self.get_serializer(auditorias, many=True)
        return Response(serializer.data)


class ConfiguracaoEscolaViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracaoEscola.objects.all()
    serializer_class = ConfiguracaoEscolaSerializer

    @action(detail=False, methods=['get'])
    def por_escola(self, request):
        """Retorna configuração de uma escola específica"""
        escola_id = request.query_params.get('escola_id')
        if not escola_id:
            return Response({'erro': 'escola_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            config = ConfiguracaoEscola.objects.get(id_escola=escola_id)
            serializer = self.get_serializer(config)
            return Response(serializer.data)
        except ConfiguracaoEscola.DoesNotExist:
            return Response({'erro': 'Configuração não encontrada'}, status=status.HTTP_404_NOT_FOUND)
