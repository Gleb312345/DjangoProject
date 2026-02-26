from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # ← ось це обов'язково
    path('', include('shop.urls')),   # твій додаток
]