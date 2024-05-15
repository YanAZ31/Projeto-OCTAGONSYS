"""
URL configuration for octagonsys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_cadastro import views
# from views import salvar
# Rotas da aplicação
urlpatterns = [
    path('admin/', admin.site.urls),
    # Página inicial provisória
    path('registerStudent',views.registerStudent,name='registerStudent'),
    # Página de Visualização de todos os alunos
    path('todos-alunos/',views.allStudents,name='allStudents'),
    # path('mostrar-todos-alunos/',views.ShowAllStudents,name='onlyShowAllStudents'),
    path('viewStudents/',views.viewStudents,name='viewStudents'),
    path('cadastro-usuario/', views.cadastro, name='cadastro'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    #Editar
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('salvar/', views.salvar ,name='salvar'),
]
