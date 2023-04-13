from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListAlunoMatriculadoSerializer, ListMatriculaAlunoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas s Matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListMatriculaAluno(generics.ListAPIView):
    """Listando matriucla de alunos"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListMatriculaAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListAlunoMaticulados(generics.ListAPIView):
    """Listando alunos matriculados"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListAlunoMatriculadoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]