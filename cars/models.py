from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    descriptio = models.CharField(max_length=200)