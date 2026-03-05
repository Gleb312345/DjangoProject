from django.shortcuts import render
from .models import Product, Category

def home(request):
    products = Product.objects.all().prefetch_related('images')
    categories = Category.objects.all()
    return render(request, "shop/home.html", {
        "products": products,
        "categories": categories
    })

def category_view(request, id):
    products = Product.objects.filter(category_id=id).prefetch_related('images')
    categories = Category.objects.all()
    return render(request, "shop/home.html", {
        "products": products,
        "categories": categories
    })