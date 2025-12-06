# Run with: python manage.py shell < scripts/load_sample.py
from shop.models import Category, Product
c1 = Category.objects.create(name='Vegetables', slug='vegetables')
c2 = Category.objects.create(name='Fruits', slug='fruits')
Product.objects.create(category=c1, name='Potato', slug='potato', description='Fresh potatoes', price=20.0, stock=100)
Product.objects.create(category=c1, name='Tomato', slug='tomato', description='Red tomatoes', price=30.0, stock=80)
Product.objects.create(category=c2, name='Apple', slug='apple', description='Fresh apples', price=50.0, stock=50)
print('Sample data created')
