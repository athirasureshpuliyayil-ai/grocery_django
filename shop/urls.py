from django.urls import path
from django.contrib.auth import views as auth_views  # ← add this import
from . import views

app_name = 'shop'

urlpatterns = [
    # 🏠 Product browsing
    path('', views.product_list, name='product_list'),
    path('category/<slug:slug>/', views.product_list, name='category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # 🛒 Cart URLs
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),

    # 💳 Checkout
    path('checkout/', views.checkout, name='checkout'),

    # 👤 Authentication & user-related
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
