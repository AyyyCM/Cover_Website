from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.home, name='project_list'),
    path('project/<int:pk>/', views.home, name='project_detail'),
]