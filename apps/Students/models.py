from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
	pariente = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	gender = models.CharField(max_length=10)