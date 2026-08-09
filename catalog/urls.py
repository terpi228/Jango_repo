#catalog/urls.py

from django.urls import path
from .views import (
    CategoryProductsView, ProductListView, ProductDetailView, ContactsView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    TogglePublishView
)
from django.views.decorators.cache import cache_page

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),   
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:product_id>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:product_id>/toggle_publish/', TogglePublishView.as_view(), name='toggle_publish'),
    path('product/<int:product_id>/', cache_page(300)(ProductDetailView.as_view()), name='product_detail'),
    path('category/<int:pk>/', CategoryProductsView.as_view(), name='category_products'),
]