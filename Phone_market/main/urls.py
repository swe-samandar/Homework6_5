from django.urls import path
from .views import main, phone_detail


urlpatterns = [
    path('', main, name='main'),
    path('phone/<int:pk>', phone_detail, name='phone_detail')
]
