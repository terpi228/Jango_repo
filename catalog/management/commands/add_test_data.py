from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Очищает базу и добавляет тестовые категории и продукты'

    def handle(self, *args, **options):
        # Удаляем все существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING('Все данные удалены'))

        # Создаём категории
        categories = [
            {'name': 'Смартфоны', 'description': 'Мобильные телефоны'},
            {'name': 'Ноутбуки', 'description': 'Портативные компьютеры'},
            {'name': 'Аксессуары', 'description': 'Чехлы, зарядки и т.д.'},
        ]
        created_cats = []
        for cat_data in categories:
            cat = Category.objects.create(**cat_data)
            created_cats.append(cat)
            self.stdout.write(f'Создана категория: {cat.name}')

        # Создаём продукты
        products = [
            {'name': 'iPhone 15', 'description': 'Флагман Apple', 'price': 999.00, 'category': created_cats[0]},
            {'name': 'Samsung Galaxy S24', 'description': 'Android флагман', 'price': 899.00, 'category': created_cats[0]},
            {'name': 'MacBook Pro', 'description': 'M3 Pro', 'price': 1999.00, 'category': created_cats[1]},
            {'name': 'Чехол для iPhone', 'description': 'Силиконовый', 'price': 19.99, 'category': created_cats[2]},
        ]
        for prod_data in products:
            Product.objects.create(**prod_data)
            self.stdout.write(f'Создан продукт: {prod_data["name"]}')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены'))