from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "status", "total_price", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["user__username", "id"]
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
