from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def CategoryList(request):
    product_categories  = ProductCategoryModel.objects.all().order_by('-created_at')
    context = {
        'product_categories': product_categories,
    }
    return render(request, 'category_list.html', context)

def CategoryCreate(request):
    if request.method == 'POST':
        product_category = ProductCategoryModel.objects.create(
            name = request.POST.get('name'),
        )
        product_category.save()
    return redirect('/category/list/')

def CategoryUpdate(request, id):
    if request.method == 'POST':
        product_category = ProductCategoryModel.objects.get(id=id)
        product_category.name = request.POST.get('name')
        product_category.save()
    return redirect('/category/list/')

def CategoryDelete(request, id):
    if request.method == 'POST':
        product_category = ProductCategoryModel.objects.get(id=id)
        product_category.delete()
    return redirect('/category/list/')

# ================================Product=======================================
def ProductList(request):
    products = ProductModel.objects.all().order_by('-created_at')
    product_categories = ProductCategoryModel.objects.all()
    context = {
        'products': products,
        'product_categories': product_categories,
    }
    return render(request, 'product_list.html', context)

def ProductCreate(request):
    if request.method == "POST":
        product = ProductModel.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            product_category_id = request.POST.get('product_category'),
        )
        product.save()
        return redirect('/product/list/')

def ProductUpdate(request, id):
    if request.method == "POST":
        product = ProductModel.objects.get(id=id)
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.product_category_id = request.POST.get('product_category')
        product.save()
    return redirect('/product/list/')

def ProductDelete(request, id):
    if request.method == "POST":
        product = ProductModel.objects.get(id=id)
        product.delete()
    return redirect('/product/list/')