from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validate the form manually
        if not first_name:
            messages.error(request, "First name is required.")
        if not last_name:
            messages.error(request, "Last name is required.")
        if not email:
            messages.error(request, "Email is required.")
        if not password:
            messages.error(request, "Password is required.")
        
        # If any field is missing, return to the registration page with errors
        if not first_name or not last_name or not email or not password:
            return redirect('register')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "The email is already registered. Please use a different one.")
            return redirect('register')

        try:
            # Create the user
            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
            messages.success(request, "Your account has been created successfully! You can now log in.")
            return redirect('login')  # Redirect to login page after successful registration
        except Exception as e:
            messages.error(request, f"Oops! Something went wrong: {str(e)}. Please try again.")
            return redirect('register')

    return render(request, 'users/register.html', {'error_messages': messages.get_messages(request)})
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        print(f"Attempting login for email: {email}")  # Debugging
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            print(f"Authentication successful! Logged in as: {user.email}, Superuser: {user.is_superuser}")
            login(request, user)  # Log the user in

            print(f"Session Key after login: {request.session.session_key}")

            # Debug: Check if user is logged in
            print(f"User after login: {request.user}, Is Superuser: {request.user.is_superuser}")

            # Display success message
            messages.success(request, f"Welcome back, {user.first_name}!")

            # Get the 'next' URL parameter from the request (this tells where to redirect after login)
            next_url = request.GET.get('next', None)  # Default to None if not found

            if next_url:
                print(f"Redirecting to next_url: {next_url}")
                return redirect(next_url)  # Redirect to the 'next' URL if it exists
            else:
                # Redirect to the appropriate page based on the user's role
                if user.is_superuser:
                    return redirect('dashboard')  # Redirect to admin dashboard
                else:
                    return redirect('cart_view')  # Redirect to user's cart view
        
        else:
            print("Authentication failed!")  # Debugging
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'users/login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


