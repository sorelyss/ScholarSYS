from django.shortcuts import render
from django import forms
from django.db import models
from apps.Students.models import Students
from django.forms import ModelForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.Students.forms import StudentsRegisterForm


	
class Register_students(CreateView):
	model = Students
	template_name = "students/register.html"
	form_class = StudentsRegisterForm
	success_url = reverse_lazy('register_student')

# Create your views here.
