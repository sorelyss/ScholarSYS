from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    url(r'^register', views.Register_student.as_view(), name = 'register_student'),
    url(r'^profile', views.Profile_student, name = 'st_profile'),
]
