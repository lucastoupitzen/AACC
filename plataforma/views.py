from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .Form.classes.Autenticador import Autenticador
from .Form.classes.Coordenador import Coordenador
from .Form.classes.Professor import Professor
from .Form.CRUD.crud_AACC import crud_AACC
from .Form.CRUD.crud_AACC_para_avaliacao import crud_AACC_para_avaliacao
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth import logout as logout_django
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/login/")
@allowed_users(["coordenador"])
def encaminhamentos(request):
    return render(request, 'encaminhamentos.html')

@login_required(login_url="/login/")
@allowed_users(["coordenador"])
def home_page(request):
    return render(request, 'home.html')

@unauthenticated_user
def cadastro(request):
    if request.method == 'GET':
        return render(request, "cadastro.html")
    
    if request.method == 'POST':
        numero_usp = request.POST.get('numerousp')
        senha = request.POST.get('senha')
        email = request.POST.get('email') 
        primeiro_nome = request.POST.get('primeiro_nome') 
        ultimo_nome = request.POST.get('ultimo_nome') 

        user = User.objects.filter(username=numero_usp).first()

        if user:
            return HttpResponse("Usuário já cadastrado no banco de dados...")
        
        user = User.objects.create_user(username=numero_usp, email=email, password=senha, first_name=primeiro_nome, last_name=ultimo_nome)
        user.save()

        return HttpResponse("Usuário cadastrado com sucesso!")

@unauthenticated_user 
def login(request):

    if request.method == 'GET':
        return render(request, "login.html")
     
    if request.method == 'POST':
        numero_usp = request.POST.get('numero_usp')
        senha = request.POST.get('senha')

        usuario = authenticate(username=numero_usp, password=senha)
        if usuario:
            login_django(request, usuario)
            return redirect("home")

        return JsonResponse({'message': 'Login errado'})  # Você pode retornar outras informações necessárias


def logout(request):
    logout_django(request)
    return redirect('login')
    
@allowed_users(["coordenador"])
def aacc_aguardando_encaminhamento(request):

    if request.method == 'GET':
        dados = crud_AACC().read_AACC_nao_delegadas()

        for chave, valor in dados.items():
            valor['doc'] = str(valor['doc'])

        dados_json = json.dumps(dados, cls=DjangoJSONEncoder)


        return JsonResponse(dados_json, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def visualizar_documento(request, nome_arquivo):
    caminho_documento = os.path.join('/home/lucas/Desktop/projetos/IC/AACC/AACC/plataforma/templates/static', 'documentos', nome_arquivo)
    with open(caminho_documento, 'rb') as documento:
        response = HttpResponse(documento.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={nome_arquivo}'
        return response
    
@allowed_users(["coordenador"])
def encaminhar(request):

    if request.method == 'POST':

        id_AACC = request.POST.get('id_AACC')
        professor = request.POST.get('professorSelecionado')
        dados = crud_AACC_para_avaliacao().create_AACC_encaminhada(id_AACC, professor)

        if dados:

            crud_AACC().update_AACC_status(id_AACC, 1)
            return JsonResponse({'success': 'Encaminhamento realizado com sucesso!'})
        else:
            return JsonResponse({'error': 'Problema ao realizar o encaminhamento!'})
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

