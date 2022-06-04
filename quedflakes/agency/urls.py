from django.urls import path, include
from . import views
#from agency.views import home

urlpatterns = [
    path('', views.home, name='home'),
]