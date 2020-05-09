from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adding/', views.adding_form, name='adding')
]
