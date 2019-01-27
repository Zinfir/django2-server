import json

from django.shortcuts import render


def contacts(request):

    context = {}

    with open('data/context.json') as file:
        context = json.load(file)

    return render(request, 'contacts/contacts.html', context)
