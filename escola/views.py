from django.http import JsonResponse
from emec.client import Institution
from escola.models import Aluno, Curso
from escola.serializer import AlunosSerializer, CursoSerializer
from rest_framework import viewsets


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# def alunos(request) :
#     if request.method == 'GET':
#       # ies = Institution(2571)
#       # ies.parse()
#       # data = ies.get_full_data()
#       aluno = {'id': 1, 'nome': 'Matheus'}
#       return JsonResponse(aluno)
