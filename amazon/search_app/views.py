from django.shortcuts import render
from flipkartapp.models import product
from django.db.models import Q

def searchresult(request):
    query = request.GET.get('q')
    if not query:
        return render(request, 'empty_search.html')  # Render a template for empty search query

    # Sanitize user input if needed

    products = product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'products': products})
