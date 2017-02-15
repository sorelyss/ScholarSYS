from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^register_student', views.Register_student.as_view(), name = 'register_student'),
    
]
