from django.shortcuts import render, get_object_or_404
from .models import Product, HeroImage
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import TeamMember
def home(request):
    products = Product.objects.all().order_by('id')
    hero_images = HeroImage.objects.all()  # Fetch hero images
    total_products = Product.objects.count()  # Get total product count
    team_members = TeamMember.objects.all()
    
    paginator = Paginator(products, 8)  # Show 8 products per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)
    
   
    return render(request, 'products/home.html', {'products': products, 'hero_images': hero_images,'total_products':total_products,'page_obj': page_obj,'team_members':team_members})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def about_us(request):
    return render(request,'products/about_us.html')


  


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # address = form.cleaned_data['address']
            inquiry = form.cleaned_data['inquiry']
            
            # Send an email to the admin
            send_mail(
    'New Contact Us Inquiry',  # Subject of the email
    f"Name: {name}\nEmail: {email}\nInquiry: {inquiry}",  # Body of the email (user's info)
    'krrishchhetri6@gmail.com',  # Send from your authenticated email address (krrishchhetri6@gmail.com)
    ['krrishchhetri6@gmail.com'],  # Send to the client's email address (this is fixed, always the client)
)


            return render(request, 'products/contact_us.html', {'form': ContactForm(), 'success': True})

    else:
        form = ContactForm()

    return render(request, 'products/contact_us.html', {'form': form})




from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import BookingForm
from .models import Product

def book_now(request, product_id):
    # Ensure product exists
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Collecting Form Data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            # Sending Email
            subject = 'New Booking Request'
            message = (
                f"New Booking Request:\n\n"
                f"Product: {product.name}\n"
                f"Price: {product.price}\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Address: {address}"
            )
            from_email = 'krrishchhetri6@gmail.com'  # Your email
            recipient_list = ['krrishchhetri6@gmail.com']

            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, "Your booking request has been submitted successfully!")
                # Redirect to a success page after the booking
                return redirect('success_page')
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")
                # Stay on the same page with an error message
                return redirect('book_now', product_id=product.id)
    else:
        form = BookingForm()

    return render(request, 'products/book_now.html', {'form': form, 'product': product})

def success_page(request):
    return render(request, 'products/success.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from .models import Product, HeroImage, TeamMember
from .forms import ProductForm, HeroImageForm, TeamMemberForm
from django.contrib.auth.decorators import login_required

def dashboard(request):
    print(f"Dashboard Session Key: {request.session.session_key}")
    print(f"Dashboard User: {request.user}, Is Superuser: {request.user.is_superuser}")
    print(f"User: {request.user}, Is Superuser: {request.user.is_superuser}")
    if not (request.user.is_superuser):
        return redirect('/')  # Redirect unauthorized users to the home page
  
    products = Product.objects.all()
    hero_images = HeroImage.objects.all()
    team_members = TeamMember.objects.all()
    return render(request, 'products/dashboard.html', {
        'products': products,
        'hero_images': hero_images,
        'team_members': team_members,
    })



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


def add_hero_image(request):
    if request.method == 'POST':
        form = HeroImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HeroImageForm()
    return render(request, 'products/add_hero_image.html', {'form': form})


def add_team_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TeamMemberForm()
    return render(request, 'products/add_team_member.html', {'form': form})

def remove_item(request, item_id):
    if request.method == 'POST':
        item_type = request.POST.get('type')  # Get item type from POST request

        try:
            if item_type == 'hero_image':
                item = get_object_or_404(HeroImage, id=item_id)
            elif item_type == 'product':
                item = get_object_or_404(Product, id=item_id)
            elif item_type == 'team_member':
                item = get_object_or_404(TeamMember, id=item_id)
            else:
                return redirect('dashboard')  # Invalid type, return to dashboard

            # Delete the item
            item.delete()
            return redirect('dashboard')  # Redirect after deleting

        except ObjectDoesNotExist:
            return redirect('dashboard')  # If item is not found, just redirect

    return redirect('dashboard')  # Handle invalid method

