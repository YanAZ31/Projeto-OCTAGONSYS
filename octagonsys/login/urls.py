from django.urls import path
from . import views
urlpatterns = [
                path('/cadastro-usuario', views.cadastro, name='cadastro'),
                path('/login', views.login, name='login')
                ]