from django.urls import path
from .views import (
    home, category_view, product_detail, categories_list,
    add_to_cart, cart_view, subscribe
)

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories_list, name='categories'),
    path('category/<int:id>/', category_view, name='category'),
    path('product/<int:id>/', product_detail, name='product'),

    # КОШИК
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),

    # РОЗСИЛКА
    path('subscribe/', subscribe, name='subscribe'),
]