from django.http import JsonResponse
from emec.client import Institution
def alunos(request) :
    if request.method == 'GET':
      # ies = Institution(2571)
      # ies.parse()
      # data = ies.get_full_data()
      aluno = {'id': 1, 'nome': 'Matheus'}
      return JsonResponse(aluno)