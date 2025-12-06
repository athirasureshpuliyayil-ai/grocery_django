from django.contrib import admin
from django.utils.html import format_html  # ✅ You must import this for image_tag to work
from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'image_tag')  # 👈 Show image preview
    prepopulated_fields = {'slug': ('name',)}

    # ✅ Optional: show image thumbnail preview in admin list view
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover; border-radius:8px;"/>',
                obj.image.url
            )
        return "-"
    image_tag.short_description = "Preview"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'status', 'total')
    inlines = [OrderItemInline]
