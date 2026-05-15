import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User

from .models import Feedback, Cesta, Perfil

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def contato(request):
    form_message = None
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        assunto = request.POST.get('assunto')
        avaliacao = request.POST.get('avaliacao')
        mensagem = request.POST.get('mensagem')

        feedback = Feedback(
            nome=nome,
            email=email,
            assunto=assunto,
            avaliacao=avaliacao,
            telefone=telefone,
            mensagem=mensagem,
        )
        feedback.save()
        
        # Simular envio de email (apenas log no console)
        print(f"Contato de {nome} ({email})")
        print(f"Telefone: {telefone}")
        print(f"Assunto: {assunto}")
        print(f"Avaliação: {avaliacao} estrelas")
        print(f"Mensagem: {mensagem}")
        
        form_message = f"Obrigado por entrar em contato, {nome}! Recebemos sua mensagem."
    
    return render(request, 'contato.html', {'form_message': form_message})

def padarias_list(request):
    padarias = [
        {
            'id': 1,
            'nome': 'Padaria do João',
            'endereco': 'Rua A, 123',
            'telefone': '(11) 98765-4321',
            'horario': '6h às 20h',
            'imagem': 'padaria1.png'
        },
        {
            'id': 2,
            'nome': 'Padaria da Maria',
            'endereco': 'Rua B, 456',
            'telefone': '(11) 99876-5432',
            'horario': '7h às 21h',
            'imagem': 'padaria2.png'
        },
        {
            'id': 3,
            'nome': 'Padaria do José',
            'endereco': 'Rua C, 789',
            'telefone': '(11) 91234-5678',
            'horario': '6h às 19h',
            'imagem': 'padaria1.png'
        }
    ]
    
    return render(request, 'padarias_list.html', {'padarias': padarias})

# CESTAS VIEWS

def cestas_list(request):
    cestas = Cesta.objects.all()
    context = {
        'cestas': cestas,
    }
    return render(request, 'cestas/list.html', context=context)


def cestas_detail(request, pk):
    cesta = get_object_or_404(Cesta, pk=pk)
    context = {
        'cesta': cesta,
    }
    return render(request, 'cestas/detail.html', context)


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_verification = request.POST.get('password_verification')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        context = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }

        if password != password_verification:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'registration/form.html', context)

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este email já está registrado.')
            return render(request, 'registration/form.html', context)

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        login(request, user)
        return redirect('dashboard_main')

    return render(request, 'registration/form.html')


@login_required
def dashboard_main(request):
    return render(request, 'dashboard/main.html')


@login_required
def perfil_update(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        perfil.telefone = request.POST.get('telefone') or None
        perfil.cpf = request.POST.get('cpf') or None
        perfil.data_nascimento = request.POST.get('data_nascimento') or None
        perfil.save()
        messages.success(request, 'Perfil atualizado com sucesso.')
        return redirect('dashboard_main')

    return render(request, 'dashboard/perfil/form.html', {'perfil': perfil})

def recipe_search(request):
    recipes = []
    query = request.GET.get('query', '')
    error_message = None
    
    if query:
        try:
            api_key = settings.SPOONACULAR_API_KEY
            url = "https://api.spoonacular.com/recipes/complexSearch"
            params = {
                'apiKey': api_key,
                'query': query,
                'number': 12,  # Number of results to return
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for 4XX/5XX responses
            
            data = response.json()
            recipes = data.get('results', [])
            total_results = data.get('totalResults', 0)
            
        except requests.RequestException as e:
            error_message = f"Não foi possível buscar receitas: {str(e)}"
    
    context = {
        'recipes': recipes,
        'query': query,
        'error_message': error_message,
    }
    
    return render(request, 'recipes/search.html', context)

