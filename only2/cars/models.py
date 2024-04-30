from django.db import models

# Create your models here.

class Cars(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_color = models.CharField(max_length=100)
    car_price = models.IntegerField()