from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.Home, name = 'home'),
    url(r'^register_user', views.Register_user.as_view(), name = 'register_user'),
    url(r'^login_user', login, {'template_name':'users/login.html'}, name = 'login_user'),
    url(r'^logout_user', logout, name = 'logout_user'),
    url(r'^user', views.Wall_user, name = 'wall_user'),
]

# {'template_name': 'users/login.html','redirect_field_name': '/'}