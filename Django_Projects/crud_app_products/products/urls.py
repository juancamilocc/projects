from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.products, name="products"),
    path("products/create/", views.create_product, name="create_product"),
    path("products/<int:product_id>/delete/", views.delete_product, name="delete_product"),
    path("products/<int:product_id>/detail/", views.update_product, name="detail_product"),
]
