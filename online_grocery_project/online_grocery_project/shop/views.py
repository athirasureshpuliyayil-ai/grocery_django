from django.shortcuts import render, get_object_or_404
from .models import Product

# 🏠 Home page view
def home(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/home.html', {'products': products})

# 🛍 Product list page
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})

# 📦 Product detail page
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})
