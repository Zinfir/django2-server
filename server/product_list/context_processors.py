from .models import Product_Category


def categories(request):
    query = Product_Category.objects.all()
    return { 'categories': query }
