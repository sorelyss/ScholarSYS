from django.shortcuts import render
from django import forms
from django.db import models
from apps.Students.models import Student
from django.forms import ModelForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.Students.forms import StudentRegisterForm


	
class Register_student(CreateView):
	model = Student
	template_name = "students/register.html"
	form_class = StudentRegisterForm
	success_url = reverse_lazy('wall_user')