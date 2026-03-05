from django.urls import path
from .views import home, category_view, product_detail, categories_list

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories_list, name='categories'),
    path('category/<int:id>/', category_view, name='category'),
    path('product/<int:id>/', product_detail, name='product'),
]