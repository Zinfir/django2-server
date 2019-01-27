import json
from functools import reduce
from django.apps import apps
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View,
)
from .models import Purchase, PurchaseItem
from .forms import PurchaseItemForm
from django.db.transaction import atomic


def cart_view(request):
    return render(request, 'cart/cart.html')


class PurchaseCreateView(LoginRequiredMixin, View):
    login_url = ''
    product_model = apps.get_model('product_detail', 'product')

    def post(self, request):
        data = json.loads(request.body)

        product_list = self.product_model.objects.filter(
            reduce(
                lambda store, key: store | Q(pk=key),
                data.keys(),
                Q()
            )
        )

        obj = Purchase.objects.create(
            user=request.user,
        )
        
        for product in product_list:
            obj.items.create(
                product=product,
                value=data[str(product.id)],
            )

        return JsonResponse(
            {
                'success_url': reverse(
                    'cart:detail',
                    kwargs={'pk': obj.id}
                )
            }
        )


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'cart/detail.html'



class PurchaseListView(ListView):
    model = Purchase
    template_name = 'cart/list.html'


# class PurchaseCreateView(CreateView):
#     model = Purchase
#     fields = ['user', 'is_active']

#     formset_model = PurchaseItem
#     formset_fields = ['product', 'value']

#     template_name = 'cart/create.html'
#     success_url = reverse_lazy('cart:list')

#     def get_formset_class(self):
#         return inlineformset_factory(
#             self.model,
#             self.formset_model,
#             fields=self.formset_fields,
#         )

#     def get_formset_kwarg(self):
#         kwargs = {}

#         if self.request.method in ('POST', 'PUT'):
#             kwargs.update({
#                 'data': self.request.POST,
#                 'files': self.request.FILES,
#             })

#         if hasattr(self, 'object'):
#             kwargs.update(
#                 **{'instance': self.object}
#             )

#         return kwargs

#     def get_formset(self):
#         formset_class = self.get_formset_class()
#         prefix = formset_class.get_default_prefix()

#         formset_kwargs = self.get_formset_kwarg()
#         formset_kwargs.update(
#             **{'prefix': prefix}
#         )

#         return formset_class(
#             **formset_kwargs
#         )

#     def get_context_data(self, **kwargs):
#         context = super(PurchaseCreateView, self).get_context_data(**kwargs)

#         context.update({
#             'formset':self.get_formset()
#         })

#         return context


#     def form_valid(self, form):
#         with atomic():
#             self.object = form.save()
#             formset = self.get_formset()

#             if formset.is_valid():
#                 formset.save()

#                 return redirect(self.success_url)

#         return render(self.request, self.template_name)


class PurchaseUpdateView(UpdateView):
    model = Purchase
    fields = ['user', 'is_active']

    formset_model = PurchaseItem
    formset_fields = ['product', 'value']

    template_name = 'cart/update.html'
    success_url = reverse_lazy('cart:list')

    def get_formset_class(self):
        return inlineformset_factory(
            self.model,
            self.formset_model,
            fields=self.formset_fields,
        )

    def get_formset_kwarg(self):
        kwargs = {}

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })

        if hasattr(self, 'object'):
            kwargs.update(
                **{'instance': self.object}
            )

        return kwargs

    def get_formset(self):
        formset_class = self.get_formset_class()
        prefix = formset_class.get_default_prefix()

        formset_kwargs = self.get_formset_kwarg()
        formset_kwargs.update(
            **{'prefix': prefix}
        )

        return formset_class(
            **formset_kwargs
        )

    def get_context_data(self, **kwargs):
        context = super(PurchaseUpdateView, self).get_context_data(**kwargs)

        context.update({
            'formset':self.get_formset()
        })

        return context


    def form_valid(self, form):
        with atomic():
            self.object = form.save()
            formset = self.get_formset()

            if formset.is_valid():
                formset.save()

                return redirect(self.success_url)

        return render(self.request, self.template_name)
