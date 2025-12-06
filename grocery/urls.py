from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views  # your app views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🏠 Home page
    path('', views.home, name='home'),

    # 🛍️ Shop app routes
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),

    # 👤 Auth system (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # 🚪 Custom logout redirect to home
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # 👤 Dashboard (optional, since it already exists in shop.urls)
    path('dashboard/', views.dashboard, name='dashboard'),
]

# ✅ Serve uploaded images and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
