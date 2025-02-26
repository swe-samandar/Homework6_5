from django.db import models
from main.models import Phone

# Create your models here.

class Dealer(models.Model):
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
    dealer_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.PositiveIntegerField()
    inventory_value = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'dealer'

    def __str__(self):
        return self.dealer_name