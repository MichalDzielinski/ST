from django.urls import path
from . import views

app_name='book'

urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),

]