from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def contato(request):
    form_message = None
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        rating = request.POST.get('rating')
        message = request.POST.get('message')
        
        # Simular envio de email (apenas log no console)
        print(f"Contato de {name} ({email})")
        print(f"Assunto: {subject}")
        print(f"Avaliação: {rating} estrelas")
        print(f"Mensagem: {message}")
        
        form_message = f"Obrigado por entrar em contato, {name}! Recebemos sua mensagem."
    
    return render(request, 'contato.html', {'form_message': form_message})