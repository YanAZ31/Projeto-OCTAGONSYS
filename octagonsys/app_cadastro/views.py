from django.shortcuts import render
# Trazendo dados para a view
# from .models import render 
from .models import Aluno
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def registerStudent(request):
    return render(request,'register/template-register-students.html')

def allStudents(request):
    novo_aluno = Aluno()
    # Recebendo dados do formulário
    novo_aluno.full_name_student = request.POST.get('fullName')
    novo_aluno.mom_name = request.POST.get('momName')
    novo_aluno.father_name = request.POST.get('fatherName')
    novo_aluno.mom_contact = request.POST.get('momContact')
    novo_aluno. father_contact = request.POST.get('fatherContact')    
    novo_aluno. mom_email = request.POST.get('momEmail')
    novo_aluno.father_email = request.POST.get('fatherEmail')
    novo_aluno.address = request.POST.get('address')
    novo_aluno.classes = request.POST.get('classes')    

    # Salvando aluno novo no db
    novo_aluno.save()
    #Retornando todos os alunos
    alunos = {
        'alunos': Aluno.objects.all()
    }
    # Indicando onde será exibido
    return render(request,'register/allStudents.html',alunos)

def viewStudents(request):
    alunos = Aluno.objects.all()
    return render(request,'register/viewStudants.html',{'alunos':alunos})

def cadastro(request):
    if request.method == "GET":
        return render(request, 'register/cadastro.html')
    else:
        usuario =  request.POST.get('usuario')
        email =  request.POST.get('email')
        senha =  request.POST.get('senha')

        user = User.objects.filter(username=usuario).first()
        # return HttpResponse(usuario)
    
        if user:
            return HttpResponse("Já existe um usuário com esse login")
    
        user = User.objects.create_user(username=usuario,email=email,password=senha)
        user.save()
        return HttpResponse("Usuário cadastrado com sucesso")
    

def login(request):
    if request.method == "GET":
        return render(request, 'register/login.html')
    
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user:
            login_django(request, user)
            return  render(request,'register/home.html')
        
        else:
            return HttpResponse("Usuário ou senha incorretos") 

@login_required        
def home(request):
    if request.user.is_authentificated:
        return render(request,'register/template-register-students.html')
    return