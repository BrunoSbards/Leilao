from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.get_leiloeiro,name='get_all_leiloeiro'),
 
    
]
