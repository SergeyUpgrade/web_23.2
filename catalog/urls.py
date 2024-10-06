from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='products_update'),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="products_delete")
]
