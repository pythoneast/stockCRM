from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Product
from .core import get_form_name
from .forms import (
    ProductForm,
    SellProductForm,
    DeleteProductForm,
    SupplierProductForm
)

from stockCRM.decorators import (
    is_anonymous,
    is_warehouse_manager,
    can_create_product,
    can_update_product,
    can_delete_product,
    can_sell_product
)


@is_anonymous
def product_list(request):
    products = Product.objects.order_by('id')
    form = SellProductForm
    delete_product_form = DeleteProductForm
    return render(request, 'products/products_list.html', locals())


@is_anonymous
def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', locals())


@can_create_product
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_create.html', locals())


@can_update_product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = get_form_name(request.user.user_type)
    form = form(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_edit.html', locals())


@can_delete_product
@require_POST
def product_delete(request):
    form = DeleteProductForm(request.POST)
    if form.is_valid():
        product = Product.objects.get(pk=form.cleaned_data['prod_id'])
        product.delete()
        return JsonResponse({'success': True, 'response': 'You have deleted the product successfully!'})
    return JsonResponse({'error': True, 'errors': form.errors})


@can_sell_product
@require_POST
def sell_product(request):
    form = SellProductForm(request.POST or None)
    if form.is_valid():
        return JsonResponse({'success': True, 'response': 'You have sold goods successfully!'})
    return JsonResponse({'error': True, 'errors': form.errors})
