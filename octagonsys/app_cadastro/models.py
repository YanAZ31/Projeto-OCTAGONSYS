from django.db import models

# Irá se transformar em uma tabela
class Aluno(models.Model):
    # Validação no backend
    id_aluno = models.AutoField(primary_key=True)
    full_name_student = models.TextField(max_length = 100)
    mom_name = models.TextField(max_length = 100)
    father_name = models.TextField(max_length = 100)
    mom_contact = models.TextField(max_length = 20)
    father_contact = models.TextField(max_length = 20)
    mom_email = models.EmailField(max_length = 30)
    father_email = models.EmailField(max_length = 30)
    address = models.TextField(max_length = 50)
    classes = models.TextField(max_length = 3)
