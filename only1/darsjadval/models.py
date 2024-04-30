from django.db import models

# Create your models here.

class Schedure(models.Model):
    name=models.CharField(max_length=255)
    time=models.IntegerField()
    its_teacher=models.CharField(max_length=255)

class Teachers(models.Model):
    full_name=models.CharField(max_length=255)
    age=models.IntegerField()
    experience=models.CharField(max_length=255)
    salary=models.IntegerField()