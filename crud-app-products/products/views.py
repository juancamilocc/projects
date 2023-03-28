from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, "products/index.html")

def products(request):
    list_products = Product.objects.all()
    return render(request, "products/products.html", {
        "products": list_products
    })

def create_product(request):
    if request.method == "GET":
        return render(request, "products/create_product.html", {
            "form": ProductForm
        })
    else:
        try:
            form = ProductForm(request.POST)
            new_product = form.save(commit=False)
            new_product.save()
            return redirect("products:products")
        except ValueError:
            return render(request, "products/create_product.html", {
                "form": ProductForm,
                "error": "Invalid data"
            })   


def update_product(request, product_id):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product)
        return render(request, "products/detail_product.html", {
            "product": product,
            "form": form
        })
    else:
        try:
            product = get_object_or_404(Product, pk=product_id)
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect("products:products")
        except ValueError:
            return render(request, "products/detail_product.html", {
                "product": product,
                "form": form,
                "error": "Error updating product"
            })

def delete_product(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect("products:products")
# Create your views here.
