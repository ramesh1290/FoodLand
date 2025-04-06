from django.contrib import admin

# Register your models here.
from .models import HeroImage,Product,TeamMember
admin.site.register(HeroImage)
admin.site.register(Product)
admin.site.register(TeamMember)