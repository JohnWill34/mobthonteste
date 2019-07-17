from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_login(request):
    return render(request, 'login.html')

def mostrar_cadastro(request):
      return render(request, 'cadastro.html')
    
def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

@csrf_protect
def submit_login(request):
  if request.POST:
      username = request.POST.get('username')
      password = request.POST.get('password')
      print(username)
      print(password)
      user = authenticate(username=username, password=password)
      if user is not None:
            login(request, user)
            return redirect('/')
      else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
  return redirect('/login/')


def mostrar_mapthon(request):
    return render(request, 'mapthon.html')