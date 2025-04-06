from django.db import models
from django.contrib.auth.models import User
class HeroImage(models.Model):
    image = models.ImageField(upload_to="hero_images/")
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else "Hero Image"

class Product(models.Model):
    name = models.CharField(max_length=200)
    model_no = models.CharField(max_length=100,default='UNKNOWN')  # Unique Model Number
    size = models.CharField(max_length=50, blank=True, null=True)  # Optional Size
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"{self.name} ({self.model_no})"
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
   
    image = models.ImageField(upload_to='team_images/')  # Store images in 'team_images/'

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('client', 'Client'), ('admin', 'Admin')])

    def __str__(self):
        return self.user.username