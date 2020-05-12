from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^select2/', include('django_select2.urls')),
    path('adding/', views.adding_form, name='adding')
]
