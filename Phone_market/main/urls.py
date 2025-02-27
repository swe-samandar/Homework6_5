from django.urls import path
from .views import main, phone_detail, phone_create,  phone_update, phone_delete


urlpatterns = [
    path('', main, name='main'),
    path('phone/<int:pk>', phone_detail, name='phone-detail'),
    path('phone-create/', phone_create, name='phone-create'),
    path('phone-update/<int:pk>', phone_update, name='phone-update'),
    path('phone-delete/<int:pk>', phone_delete, name='phone-delete'),
]