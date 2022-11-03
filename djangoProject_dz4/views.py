from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from user.views import random_cost


def homepage(request: HttpRequest) -> HttpResponse:

    user = {
        'username': 'Anonim user',

        'cost_item': random_cost,
        'item_name': ['Rozenta', 'Roznica', 'Comfy'],

    }
    return render(request, 'Homepage.html', user)