"""
Контроллер для страницы детального описания продукта
"""
import json
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView
)
from django.http import JsonResponse
from functools import reduce
from django.db.models import Q
from accounts.mixins import AdminGroupRequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from product_list.models import Product_Category
from product_detail.models import Product
from product_detail.forms import Product_Form
from django.core.cache import cache
from django.views.decorators.cache import cache_page


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_detail/product_list.html"
    context_object_name = 'results'
    paginate_by = 6

    def get_queryset(self):
        return self.model.objects.select_related('images').all()


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail/product_detail.html"
    context_object_name = 'instance'


class ProductCreateView(LoginRequiredMixin, AdminGroupRequired, CreateView):
    model = Product
    template_name = "product_detail/product_create.html"
    form_class = Product_Form
    redirect_url = reverse_lazy('main:main')
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    login_url = reverse_lazy('accounts:login')


class ProductUpdateView(LoginRequiredMixin, AdminGroupRequired, UpdateView):
    queryset = Product.objects.filter(is_active=True)
    template_name = "product_detail/product_create.html"
    form_class = Product_Form
    redirect_url = reverse_lazy('main:main')
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    login_url = reverse_lazy('accounts:login')


class ProductDeleteView(LoginRequiredMixin, AdminGroupRequired, DeleteView):
    queryset = Product.objects.filter(is_active=True)
    template_name = 'product_detail/product_delete.html'
    redirect_url = reverse_lazy('main:main')
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    login_url = reverse_lazy('accounts:login')
    context_object_name = 'instance'

@cache_page(3600)
def product_list(request, pk):

    context = {}

    if pk == 1:
        query = Product.objects.filter(is_active=True)
    else:
        query = Product.objects.filter(is_active=True, product_category=pk)
    paginator = Paginator(query, 6)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    static_products_on_page = []
    static_products_on_page += Product.objects.filter(name='Red Iron Chair')
    static_products_on_page += Product.objects.filter(name='Wooden Arm Chair')

    obj = get_object_or_404(Product_Category, pk=pk)

    context["results"] = items
    context["static_products_on_page"] = static_products_on_page
    context["instance"] = obj

    return render(request, "product_detail/product_list.html", context)


def product_detail(request, pk):
    """
    Рендеринг страницы детального описания продукта

    Args:
        request (str): запрос пользователя

    Returns:
        product_detail.html: страница html с подробным описанием товара
    """

    context = {}

    obj = get_object_or_404(Product, pk=pk, is_active=True)
    context["instance"] = obj

    return render(request, "product_detail/product_detail.html", context)


def product_create(request):

    template_name = "product_detail/product_create.html"
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    form = Product_Form(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})


def product_update(request, pk):
    template_name = "product_detail/product_create.html"
    success_url = reverse_lazy('product_detail:product_detail', kwargs={'pk': pk})
    prod = get_object_or_404(Product, pk=pk)
    form = Product_Form(instance=prod)

    if request.method == 'POST':
        form = Product_Form(
            request.POST,
            instance=prod
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})


@login_required(login_url=reverse_lazy('accounts:login'))
def product_delete(request, pk):
    template_name = "product_detail/product_delete.html"
    success_url = reverse_lazy('product_list:product_category', kwargs={'pk': 1})
    obj = get_object_or_404(Product, pk=pk, is_active=True)

    if request.method == 'POST':
        obj.is_active = False

        obj.save()

        return redirect(success_url)

    return render(request, template_name, {'instance': obj})


def product_json_list(request):
    query_params = (
        (key, list(map(int, value.split(','))) if key.endswith('_in') else value)
        for key, value in request.GET.items()
    )
    query = get_list_or_404(
        Product,
        reduce(
            lambda store, itm: store | Q(**{itm[0]: itm[1]}),
            query_params,
            Q()
        )
    )

    return JsonResponse(
        list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name
                },
                query
            )
        ),
        safe=False
    )