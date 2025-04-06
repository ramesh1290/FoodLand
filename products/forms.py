# products/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
   
    inquiry = forms.CharField(widget=forms.Textarea)

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))




# products/forms.py
from django import forms
from .models import Product, HeroImage, TeamMember

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'model_no', 'size', 'price', 'image']

# Hero Image Form
class HeroImageForm(forms.ModelForm):
    class Meta:
        model = HeroImage
        fields = ['image', 'caption']

# Team Member Form
class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'image']
