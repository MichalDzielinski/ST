from django.urls import path
from . import views 

app_name='authors'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('author/<int:pk>/', views.detail, name='detail'),
]