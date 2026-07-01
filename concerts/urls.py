from django.urls import path
from . import views

urlpatterns = [
    path('', views.concert_list, name='concert_list'),
]
