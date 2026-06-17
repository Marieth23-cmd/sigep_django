from datetime import date

from django.db.models import Q
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


ESCOLA_FIXA_ID = 3

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
    serializer_class = CursoSerializer

    def get_queryset(self):
        return Curso.objects.filter(id_escola_id=ESCOLA_FIXA_ID)


class TurmaViewSet(viewsets.ModelViewSet):
    serializer_class = TurmaSerializer

    def get_queryset(self):
        return Turma.objects.filter(id_escola_id=ESCOLA_FIXA_ID)

    @action(detail=True, methods=['get'])
    def alunos(self, request, pk=None):
        turma = self.get_object()

        alunos = Aluno.objects.filter(
            id_turma=turma,
            id_escola_id=ESCOLA_FIXA_ID
        )

        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)


class BolsaViewSet(viewsets.ModelViewSet):
    serializer_class = BolsaSerializer

    def get_queryset(self):
        return Bolsa.objects.filter(id_escola_id=ESCOLA_FIXA_ID)


class AlunoViewSet(viewsets.ModelViewSet):
    serializer_class = AlunoSerializer

    def get_queryset(self):
        queryset = (
            Aluno.objects
            .filter(id_escola_id=ESCOLA_FIXA_ID)
            .select_related(
                'id_escola',
                'id_turma',
                'id_turma__id_curso',
                'id_bolsa'
            )
            .order_by('nome', 'numero_aluno')
        )

        termo = self.request.query_params.get('search')

        if termo:
            termo_limpo = termo.replace('#', '').strip()

            filtro = (
                Q(nome__icontains=termo) |
                Q(id_turma__nome__icontains=termo) |
                Q(id_turma__id_curso__nome__icontains=termo)
            )

            if termo_limpo.isdigit():
                filtro |= Q(numero_aluno=int(termo_limpo))

            queryset = queryset.filter(filtro)

        return queryset

    @action(detail=False, methods=['get'])
    def por_turma(self, request):
        turma_id = request.query_params.get('turma_id')

        if not turma_id:
            return Response(
                {'erro': 'turma_id é obrigatório'},
                status=status.HTTP_400_BAD_REQUEST
            )

        alunos = Aluno.objects.filter(
            id_turma=turma_id,
            id_escola_id=ESCOLA_FIXA_ID
        )

        serializer = self.get_serializer(alunos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def pagamentos(self, request, pk=None):
        aluno = self.get_object()

        pagamentos = Pagamento.objects.filter(
            id_aluno=aluno
        )

        serializer = PagamentoSerializer(
            pagamentos,
            many=True
        )

        return Response(serializer.data)


class PagamentoViewSet(viewsets.ModelViewSet):
    serializer_class = PagamentoSerializer

    def get_queryset(self):
        return (
            Pagamento.objects
            .filter(id_aluno__id_escola_id=ESCOLA_FIXA_ID)
            .select_related(
                'id_aluno',
                'id_aluno__id_turma',
                'id_aluno__id_turma__id_curso'
            )
            .order_by(
                '-ano',
                '-mes',
                '-data_pagamento',
                '-id_pagamento'
            )
        )

    @action(detail=False, methods=['get'])
    def por_aluno(self, request):
        aluno_id = request.query_params.get('aluno_id')

        if not aluno_id:
            return Response(
                {'erro': 'aluno_id é obrigatório'},
                status=status.HTTP_400_BAD_REQUEST
            )

        pagamentos = self.get_queryset().filter(
            id_aluno=aluno_id
        )

        serializer = self.get_serializer(
            pagamentos,
            many=True
        )

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def por_mes_ano(self, request):
        mes = request.query_params.get('mes')
        ano = request.query_params.get('ano')

        if not mes or not ano:
            return Response(
                {'erro': 'mes e ano são obrigatórios'},
                status=status.HTTP_400_BAD_REQUEST
            )

        pagamentos = self.get_queryset().filter(
            mes=mes,
            ano=ano
        )

        serializer = self.get_serializer(
            pagamentos,
            many=True
        )

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def resumo(self, request):
        mes = request.query_params.get('mes')
        ano = request.query_params.get('ano')

        if not mes or not ano:
            return Response(
                {'erro': 'mes e ano sao obrigatorios'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            mes = int(mes)
            ano = int(ano)
        except ValueError:
            return Response(
                {'erro': 'mes e ano devem ser numericos'},
                status=status.HTTP_400_BAD_REQUEST
            )

        alunos_ativos = Aluno.objects.filter(
            estado='ACTIVO',
            id_escola_id=ESCOLA_FIXA_ID
        )

        total_alunos = alunos_ativos.count()

        alunos_pagos_ids = set(
            self.get_queryset()
            .filter(
                mes=mes,
                ano=ano,
                id_aluno__estado='ACTIVO'
            )
            .values_list('id_aluno_id', flat=True)
        )

        hoje = date.today()

        meses_vencidos = []

        if ano < hoje.year:
            meses_vencidos = list(range(1, 13))
        elif ano == hoje.year:
            meses_vencidos = list(range(1, hoje.month))

        atrasados = 0

        if meses_vencidos:
            pagamentos_vencidos = set(
                self.get_queryset()
                .filter(
                    ano=ano,
                    mes__in=meses_vencidos,
                    id_aluno__estado='ACTIVO'
                )
                .values_list('id_aluno_id', 'mes')
            )

            for aluno_id in alunos_ativos.values_list(
                'id_aluno',
                flat=True
            ):
                if any(
                    (aluno_id, mes_vencido)
                    not in pagamentos_vencidos
                    for mes_vencido in meses_vencidos
                ):
                    atrasados += 1

        pagos = len(alunos_pagos_ids)

        em_falta = max(
            total_alunos - pagos,
            0
        )

        return Response({
            'total_alunos': total_alunos,
            'pagos': pagos,
            'em_falta': em_falta,
            'atrasados': atrasados,
            'mes': mes,
            'ano': ano,
        })


class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer


class ConfiguracaoEscolaViewSet(viewsets.ModelViewSet):
    serializer_class = ConfiguracaoEscolaSerializer

    def get_queryset(self):
        return ConfiguracaoEscola.objects.filter(
            id_escola_id=ESCOLA_FIXA_ID
        )