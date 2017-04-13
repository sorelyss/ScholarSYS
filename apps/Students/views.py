from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django import forms
from django.db import models
from apps.Students.models import Student
from django.forms import ModelForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.Students.forms import StudentRegisterForm
from django.contrib.auth.decorators import login_required

#@login_required(login_url=reverse_lazy('login_user'))
class Register_student(CreateView):
	model = Student
	template_name = "students/register.html"
	form_class = StudentRegisterForm
	success_url = reverse_lazy('wall_user')

def Profile_student(request):
	st = Student.objects.get(id=request.GET['id'])
	if st.pariente_id == request.user.id:
		return render(request,'students/profile.html',{'student': st})
	else:
		return HttpResponse("No tiene permiso")