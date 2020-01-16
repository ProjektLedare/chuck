from django.urls import path

from . import views

urlpatterns = [
path('account', views.login, name='login'),
path('ren', views.ren, name='ren'),
path('', views.login, name='login'),



]