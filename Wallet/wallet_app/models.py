from django.db import models

# Create your models here.

class wallet(models.Model):  
    id = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    #user_name = models.CharField(max_length=50)
    #password = models.CharField(max_length=50)
    state = models.BooleanField(default=False)
    balance = models.FloatField(max_length=20, default=0)
