from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:product_id>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
