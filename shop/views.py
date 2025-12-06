from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import login
from .forms import CheckoutForm, RegisterForm  # ✅ fixed import
from .models import Product, Order, OrderItem, Category


# ---------- 🏠 Home Page ----------
def home(request):
    """Homepage: shows all products"""
    if not request.user.is_authenticated and 'logout' in request.META.get('HTTP_REFERER', ''):
        messages.success(request, "You have been logged out successfully!")

    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/home.html', {
        'categories': categories,
        'products': products
    })


# ---------- 🛒 Product List ----------
def product_list(request, slug=None):
    """Display all products or filter by category."""
    products = Product.objects.all()
    category = None

    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)

    # Optional search
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    categories = Category.objects.all()

    return render(request, 'shop/product_list.html', {
        'products': products,
        'categories': categories,
        'category': category,
    })


# ---------- 🧾 Product Detail ----------
def product_detail(request, slug):
    """Display a single product by its slug."""
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'categories': categories
    })


# ---------- 🛍️ CART SYSTEM ----------
def cart_add(request, product_id):
    """Add a product to the shopping cart."""
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    cart[product_id] = cart.get(product_id, 0) + 1  # Increment quantity
    request.session['cart'] = cart
    messages.success(request, "Product added to cart.")
    return redirect('shop:cart_detail')


def cart_remove(request, product_id):
    """Remove one quantity of a product from the cart."""
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]
        request.session['cart'] = cart
        messages.info(request, "Product removed from cart.")
    return redirect('shop:cart_detail')


def cart_clear(request):
    """Clear the entire cart."""
    request.session['cart'] = {}
    messages.info(request, "Cart cleared.")
    return redirect('shop:cart_detail')


def cart_detail(request):
    """Display all cart items and total price."""
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=int(pid))
        subtotal = product.price * qty
        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'shop/cart_detail.html', {
        'items': items,
        'total': total
    })


# ---------- 💳 Checkout ----------
@login_required
@transaction.atomic
def checkout(request):
    """Handles checkout process — form submission and order creation."""
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('shop:cart_detail')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # ✅ Calculate total
            total = sum(
                get_object_or_404(Product, pk=int(pid)).price * qty
                for pid, qty in cart.items()
            )

            # ✅ Create Order
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
                total=total
            )

            # ✅ Create Order Items
            for pid, qty in cart.items():
                product = get_object_or_404(Product, pk=int(pid))
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=qty
                )
                # Reduce stock
                product.stock -= qty
                product.save()

            # ✅ Clear cart after order success
            request.session['cart'] = {}
            messages.success(request, "✅ Payment successful! Your order has been placed.")

            return render(request, 'shop/order_success.html', {'order': order})
    else:
        form = CheckoutForm()

    # ✅ Cart summary for display
    items = []
    total = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=int(pid))
        subtotal = product.price * qty
        items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
        total += subtotal

    return render(request, 'shop/checkout.html', {
        'form': form,
        'items': items,
        'total': total
    })


# ---------- 👤 User Registration ----------
def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "🎉 Registration successful! Welcome aboard.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'shop/register.html', {'form': form})


# ---------- 👤 User Dashboard ----------
@login_required
def dashboard(request):
    """Simple dashboard showing user's orders."""
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'shop/dashboard.html', {'orders': orders})


# ---------- ✏️ Edit Profile ----------
@login_required
def edit_profile(request):
    """Placeholder for future profile edit view."""
    messages.info(request, "Profile editing coming soon!")
    return redirect('shop:dashboard')
