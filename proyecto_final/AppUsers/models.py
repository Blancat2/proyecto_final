from django.db import models

class Users(models.Model):
    name_user=models.CharField(max_length=40)
    password=models.CharField(max_length=40)


class Admin(models.Model):
    name_admin=models.CharField(max_length=40)
    password_admin=models.CharField(max_length=40)

class Avatar(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
   

class Blogs(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=100)
    fecha = models.TimeField(auto_now=False)
    imagen_user = models.ImageField()

