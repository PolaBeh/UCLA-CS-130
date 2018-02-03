from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-view'),
    path('<workplace_id>/', views.workplace, name='main-view'),
]
