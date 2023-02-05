from django.http import JsonResponse
from emec.client import Institution
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunosSerializer, CursoSerializer, MatriculaSerializer, MatriculasAlunoSerializer, AlunosMatriculasSerializer
from rest_framework import viewsets, generics


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasAluno(generics.ListAPIView):
    """Exibindo todas as matrículas de um aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = MatriculasAlunoSerializer


class AlunosMatriculados(generics.ListAPIView):
    """Exibindo alunos e alunas matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = AlunosMatriculasSerializer


# def alunos(request) :
#     if request.method == 'GET':
#       # ies = Institution(2571)
#       # ies.parse()
#       # data = ies.get_full_data()
#       aluno = {'id': 1, 'nome': 'Matheus'}
#       return JsonResponse(aluno)
