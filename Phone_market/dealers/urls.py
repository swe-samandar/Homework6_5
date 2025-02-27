from django.urls import path
from .views import show_dealers

urlpatterns = [
    path('all-dealers/', show_dealers, name='show-dealers')
]