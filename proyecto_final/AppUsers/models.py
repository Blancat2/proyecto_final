from django.db import models

class Users(models.Model):
    name_user=models.CharField(max_length=40)
    password=models.CharField(max_length=40)


class Admin(models.Model):
    name_admin=models.CharField(max_length=40)
    password=models.CharField(max_length=40)