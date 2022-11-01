from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='views'),
    path('contact/', views.contact, name='views'),
]
