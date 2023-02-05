from rest_framework import serializers
from escola.models import Aluno, Curso


class AlunosSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Aluno 
        fields= ['id', 'node', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Curso
        fields = '__all__'