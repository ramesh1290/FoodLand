from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product

@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).first()  # Fetch user's cart

    if cart:
        cart_items = cart.cartitems.all()
        print(f"Cart ID: {cart.id}, Total Items: {cart_items.count()}")
    else:
        cart_items = []
        print("No cart found for user!")

    return render(request, "cart/cart.html", {"cart": cart, "cart_items": cart_items})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_cart_id = request.session.get('cart_id')
        cart, created = Cart.objects.get_or_create(id=session_cart_id) if session_cart_id else Cart.objects.create()
        request.session['cart_id'] = cart.id  # Store cart ID in session

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart_view")


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.cart.user == request.user:
        cart_item.delete()
    return redirect("cart_view")

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart_item.quantity = max(1, quantity)
        cart_item.save()
    return redirect("cart_view")


