from django.shortcuts import render, get_object_or_404
from .models import Product, HeroImage

def home(request):
    products = Product.objects.all()
    hero_images = HeroImage.objects.all()  # Fetch hero images
    total_products = Product.objects.count()  # Get total product count

    return render(request, 'products/home.html', {'products': products, 'hero_images': hero_images,'total_products':total_products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

