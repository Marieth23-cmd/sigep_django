from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import (
    EscolaViewSet,
    UsuarioViewSet,
    CursoViewSet,
    TurmaViewSet,
    BolsaViewSet,
    AlunoViewSet,
    PagamentoViewSet,
    AuditoriaViewSet,
    ConfiguracaoEscolaViewSet,
)

router = DefaultRouter()
router.register(r'escolas', EscolaViewSet, basename='escola')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'turmas', TurmaViewSet, basename='turma')
router.register(r'bolsas', BolsaViewSet, basename='bolsa')
router.register(r'alunos', AlunoViewSet, basename='aluno')
router.register(r'pagamentos', PagamentoViewSet, basename='pagamento')
router.register(r'auditorias', AuditoriaViewSet, basename='auditoria')
router.register(r'configuracoes', ConfiguracaoEscolaViewSet, basename='configuracao')

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
]
 