from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Product, Contact
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all().order_by('-created_at')
        if not self.request.user.has_perm('catalog.can_unpublish_product'):
            queryset = queryset.filter(is_published=True)
        return queryset[:5]


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    pk_url_kwarg = 'product_id'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        if not self.request.user.has_perm('catalog.can_unpublish_product'):
            form.fields.pop('is_published', None)
        return form

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("У вас нет прав на редактирование этого продукта.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'product_id': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class TogglePublishView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("Недостаточно прав для изменения статуса публикации.")
        product.is_published = not product.is_published
        product.save()
        return redirect('catalog:product_detail', product_id=product.pk)