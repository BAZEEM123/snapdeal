from django.shortcuts import render, get_object_or_404
from .models import category, product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def allproductCat(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug is not None:
        c_page = get_object_or_404(category, slug=c_slug)
        products_list = product.objects.filter(category=c_page, available=True)
    else:
        products_list = product.objects.filter(available=True)

    paginator = Paginator(products_list, 6)

    try:
        page = int(request.GET.get('page', 1))
    except (ValueError, TypeError):
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'products': products})

def proDetail(request, c_slug, product_slug):
    try:
        products = product.objects.get(category__slug=c_slug, slug=product_slug)
    except product.DoesNotExist:
        return render(request, '404.html')  # Render a custom 404 page
    return render(request, 'product.html', {'product': products})
