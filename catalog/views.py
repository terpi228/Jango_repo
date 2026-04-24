from django.shortcuts import render, get_object_or_404
from .models import Product, Contact


def home(request):
    products = Product.objects.all().order_by('-created_at')[:5]
    for p in products:
        print(f"На главной: {p.name} — {p.price} руб.")
    return render(request, 'catalog/home.html', {'products': products})


def contacts(request):
    contact = Contact.objects.first()
    message_sent = False

    if request.method == 'POST':
        # Здесь можно добавить логику отправки (пока просто заглушка)
        message_sent = True

    return render(request, 'catalog/contacts.html', {
        'contact': contact,
        'message_sent': message_sent
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})