from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ContactsView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:product_id>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:product_id>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]