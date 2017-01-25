from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.Users.forms import UserRegisterForm
from django.contrib.auth.views import login


def Home(request):
	return render(request, 'home.html')

def login(request,redirect_authenticated_user=False):
	return render(request, 'users/login.html', {'form':AuthenticationForm,'next':'/register_user'})
	
class Register_user(CreateView):
	model = User
	template_name = "users/register.html"
	form_class = UserRegisterForm
	success_url = reverse_lazy('home')