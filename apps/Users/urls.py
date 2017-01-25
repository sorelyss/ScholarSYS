from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name = 'home'),
    url(r'^register_user', views.Register_user.as_view(), name = 'register_user'),
    url(r'^login_user', views.login, name = 'login_user'),
]

# {'template_name': 'users/login.html','redirect_field_name': '/'}