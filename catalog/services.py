# catalog/services.py

from django.core.cache import cache
from .models import Product

def get_products_by_category(category_id):
    """
    Возвращает список опубликованных продуктов для указанной категории.
    Результат кешируется на 5 минут.
    """
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(
            category_id=category_id,
            is_published=True
        ).select_related('category'))
        cache.set(cache_key, products, 300)  #5 минут
    return products