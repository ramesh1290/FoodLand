from django.urls import path
from .views import home, product_detail,about_us,contact_us,book_now,success_page,dashboard,add_product,add_hero_image,add_team_member,remove_item

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('about_us/',about_us,name='about_us'),
   
    path('contact_us/',contact_us,name='contact_us'),
    path('product/<int:product_id>/book/', book_now, name='book_now'),
    path('success/', success_page, name='success_page'),


    path('dashboard/', dashboard, name='dashboard'),
    path('add_product/', add_product, name='add_product'),
    path('add_hero_image/', add_hero_image, name='add_hero_image'),
    path('add_team_member/', add_team_member, name='add_team_member'),
   path('remove_item/<int:item_id>/',remove_item, name='remove_item'),
]
