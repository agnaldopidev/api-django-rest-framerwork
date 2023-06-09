
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet, ListMatriculaAluno, ListAlunoMaticulados
from rest_framework import routers


router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas', ListMatriculaAluno.as_view()),
    path('cursos/<int:pk>/matriculas', ListAlunoMaticulados.as_view()),
]