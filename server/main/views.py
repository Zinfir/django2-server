from django.shortcuts import render, get_list_or_404, get_object_or_404

from django.http import HttpResponse, JsonResponse

from django.template import Template, Context

from product_list.models import Product_Category
from product_detail.models import Product

import json

from django.core.paginator import Paginator


def index(request):

    context = {}

    with open('data/context.json') as file:
        context = json.load(file)

    products = []
    products += Product.objects.filter(name='Lamp')
    products += Product.objects.filter(name='Blue Arm Chair')
    products += Product.objects.filter(name='Jugful')
    products += Product.objects.filter(name='Red Full Iron Chair')

    products += Product.objects.filter(name='Red Iron Chair')
    products += Product.objects.filter(name='Wooden Arm Chair')

    products += Product.objects.filter(name='Hanging Lamp')
    products += Product.objects.filter(name='White Arm Chair')
    products += Product.objects.filter(name='Table Lamp')
    products += Product.objects.filter(name='Wall Lamp')
    products += Product.objects.filter(name='Mortar and Pestle')
    products += Product.objects.filter(name='White Vase')

    products += Product.objects.filter(name='Wooden Circle Table')

    products += Product.objects.filter(name='Red Pillow')

    products += Product.objects.filter(name='Floor Lamp')
    products += Product.objects.filter(name='Grey Sofa')
    products += Product.objects.filter(name='Wall Clock')
    products += Product.objects.filter(name='Ceiling Black Lamp')

    context["main_products"] = products

    main_title_product = []
    main_title_product += Product.objects.filter(name='Fishnet Chair')
    context["main_title_product"] = main_title_product

    return render(request, 'main/index.html', context)


def test(request):
    query = get_list_or_404(Product)
    paginator = Paginator(query, 6)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    return render(request, "main/test.html", {'results': items})