from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(''+'authorization.html', views.authorization, name='authorization'),
    path(''+'registration.html', views.registration, name='registration'),
]