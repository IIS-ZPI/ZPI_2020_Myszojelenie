from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='base.html'), name='baza'),
    path('', views.index, name='index'),
    path('adding/', views.adding_form, name='adding')
]
