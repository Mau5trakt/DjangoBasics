from .views import *
from django.urls import path
urlpatterns = [
    path('', index, name='index'),
    path('wilmer', wilmer, name='wilmer'),
    path('saludo/<str:nombre>', saludo, name='saludo'),
    path('tichers', tichers, name='tichers')
]