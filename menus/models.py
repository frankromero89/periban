from django.db import models
from django.utils import timezone

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50, blank=False, default='Comidas')
    subtitle = models.CharField(blank=True, null=True, max_length=50)
    image = models.ImageField(upload_to='menus/images')

    def __str__(self):
        return self.name

class Platillo(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, default="nombre")
    url_name = models.CharField(max_length=50, blank=False, default="")
    description = models.TextField(blank=False, default="descripción")
    costo = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default="1.00")
    little_image = models.ImageField(upload_to='menus/images/platillos')
    big_image = models.ImageField(upload_to='menus/images/platillos')
    created = models.DateTimeField(default= timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name