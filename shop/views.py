from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review, Subscriber, CartItem


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


# ДЕТАЛЬНИЙ ТОВАР + ОЦІНКА
def product_detail(request, id):
    product = get_object_or_404(Product.objects.prefetch_related('images'), id=id)
    categories = Category.objects.all()

    # ДОДАВАННЯ ВІДГУКУ / ОЦІНКИ
    if request.method == "POST" and "rating" in request.POST:
        rating = request.POST.get("rating")
        text = request.POST.get("text", "")

        Review.objects.create(
            product=product,
            rating=rating,
            text=text
        )
        return redirect("product", id=product.id)

    return render(request, "shop/product_detail.html", {
        "product": product,
        "categories": categories
    })


# СПИСОК КАТЕГОРІЙ
def categories_list(request):
    categories = Category.objects.all()
    return render(request, "shop/categories.html", {
        "categories": categories
    })


# КОШИК
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart")


def cart_view(request):
    items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in items)

    return render(request, "shop/cart.html", {
        "items": items,
        "total": total
    })


# РОЗСИЛКА
def subscribe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        Subscriber.objects.get_or_create(name=name, email=email)

        return redirect("home")

    return redirect("home")