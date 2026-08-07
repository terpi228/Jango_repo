from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', RedirectView.as_view(url='/', permanent=False)),
    path('users/', include('users.urls')),
    path('', include('catalog.urls')), 
    path('blog/', include('blog.urls')),
]