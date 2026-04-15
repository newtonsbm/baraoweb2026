from django.shortcuts import render

from .models import Feedback

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