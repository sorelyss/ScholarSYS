from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login_school', views.Home, name = 'login_school'),
]
