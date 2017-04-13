from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.Users.forms import UserRegisterForm
from apps.Students.models import Student
from django.contrib.auth.decorators import login_required


def Home(request):
	return render(request, 'home.html')
	
class Register_user(CreateView):
	model = User
	template_name = "users/register.html"
	form_class = UserRegisterForm
	success_url = reverse_lazy('login_user')

# OJOOOOOOO
# Hacer variable la navbar incluso cuando es home... es decir mandar a todas las views el request.user
# link bueno :v http://jinja.pocoo.org/docs/2.9/templates/
@login_required(login_url=reverse_lazy('login_user'))
def Wall_user(request):
	students = Student.objects.all().filter(pariente_id=request.user.id)
	return render(request, 'users/wall.html',{'students':students})
	#return render(request, 'users/wall.html',{'user':request.user})

def GooglePlaces(request):
	return render(request, 'places.html')