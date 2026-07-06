from django.views.generic import ListView, DetailView, View, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product, Contact
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')[:5]


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        contact = Contact.objects.first()
        return render(request, self.template_name, {
            'contact': contact,
            'message_sent': False,
        })

    def post(self, request):
        contact = Contact.objects.first()
        return render(request, self.template_name, {
            'contact': contact,
            'message_sent': True,
        })


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')