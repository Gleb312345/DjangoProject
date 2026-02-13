from django.shortcuts import render

def home(request):
    pages = [
        {"name": "Товари", "url": "products"},
        {"name": "Про нас", "url": "about"},
        {"name": "Контакти", "url": "contacts"},
    ]
    return render(request, "shop/home.html", {"pages": pages})


def page(request, title):
    return render(request, "shop/page.html", {"title": title})
