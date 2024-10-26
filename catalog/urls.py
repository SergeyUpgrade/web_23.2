from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("catalog/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete")
]
