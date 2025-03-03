from django.db import models

class HeroImage(models.Model):
    image = models.ImageField(upload_to="hero_images/")
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else "Hero Image"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return self.name
