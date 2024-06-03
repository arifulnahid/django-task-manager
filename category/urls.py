from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('add-category/', views.add_category, name='add_category'),
]
