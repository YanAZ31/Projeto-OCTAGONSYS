from django.shortcuts import render
# Trazendo dados para a view
# from .models import render 
from .models import Aluno
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
