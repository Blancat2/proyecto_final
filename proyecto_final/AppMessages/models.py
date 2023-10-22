from django.db import models

# Create your models here.
class Messages(models.Model):
    message=models.CharField(max_length=80)