from django.shortcuts import render
from .models import Product, Category, Tag
from django.db.models import Q


def product_list(request):
    category_id = request.GET.get('category')
    tag_ids = request.GET.getlist('tags') 
    search_query = request.GET.get('search', '').strip()
    products = Product.objects.all()

    if search_query:
        products = products.filter(
            Q(description__icontains=search_query) |
            Q(name__icontains=search_query)
        )

    # Filter by category
    if category_id:
        products = products.filter(category_id=category_id)

    # Filter by tags (products that have all selected tags)
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_tags': tag_ids,
    }
    return render(request, 'products.html', context)


