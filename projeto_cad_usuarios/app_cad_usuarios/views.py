from django.shortcuts import render, redirect
from .models import Usuario

def home(request):  
    return render(request, 'usuarios/index.html')

def save_usuario(nome, idade):
    if not Usuario.objects.filter(nome=nome, idade=idade).exists():
        Usuario.objects.create(nome=nome, idade=idade)
        return True
    return False

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        if nome and idade:
            if save_usuario(nome, idade):
                return redirect('usuarios')

    usuarios_distintos = {usuario.nome: usuario for usuario in Usuario.objects.all()}.values()
    usuarios = {'usuarios': usuarios_distintos}
    return render(request, 'usuarios/usuarios.html', usuarios)


