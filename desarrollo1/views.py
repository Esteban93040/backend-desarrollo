from django.shortcuts import render, redirect
from desarrollo1.users import *

def ListarUsuarios(request):
    users = User.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': users})

def CrearUsuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        phone = request.POST['phone']
        is_boss = request.POST['is_boss']
        user = User(email=email, name=name, password=password, phone=phone, is_boss=is_boss)
        if email.is_valid():
            user.save()
            return redirect('listar_usuarios')
        else:
            return render(request, 'crear_usuario.html')

def EditarUsuario(request, email):
    user = User.objects.get(email=email)
    if request.method == 'GET':
        return render(request, 'editar_usuario.html', {'usuario': user})
    else:
        user.email = request.POST['email']
        user.name = request.POST['name']
        user.password = request.POST['password']
        user.phone = request.POST['phone']
        user.is_boss = request.POST['is_boss']
        user.save()
        return redirect('listar_usuarios')

def EliminarUsuario(request, email):
    user = User.objects.get(email=email)
    if request.method == 'POST':
        user.delete()
        return redirect('listar_usuarios')
    else:
        return render(request, 'eliminar_usuario.html', {'usuario': user})
# Create your views here

