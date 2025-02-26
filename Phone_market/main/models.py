from django.db import models

# Create your models here.

class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    storage_capacity = models.CharField(max_length=6)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    screen_size = models.CharField(max_length=10)
    battery_capacity = models.PositiveIntegerField()
    processor = models.CharField(max_length=25)
    camera_resolution = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='phone_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'phone'

    def __str__(self):
        ordering = ['-created_at']
        return f"{self.model} ({self.brand})"