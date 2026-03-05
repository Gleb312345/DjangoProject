from django.shortcuts import render, get_object_or_404
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


def product_detail(request, id):
    product = get_object_or_404(Product.objects.prefetch_related('images'), id=id)
    categories = Category.objects.all()

    return render(request, "shop/product_detail.html", {
        "product": product,
        "categories": categories
    })
def categories_list(request):
    categories = Category.objects.all()
    return render(request, "shop/categories.html", {
        "categories": categories
    })