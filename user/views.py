from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

# Create your views here.


def random_cost():
    cost = random.randint(10000, 20000)
    return cost


def homepage_views(request: HttpRequest, username: str) -> HttpResponse:


    custom_ctx_obj = {
        'username': username,

        'cost_item': random_cost,
        'item_name': ['Rozenta', 'Roznica', 'Comfy'],

    }
    return render(request, 'Homepage.html', custom_ctx_obj)


def u_profile(request: HttpRequest, profile: str) -> HttpResponse:
    profile_name = {
        'username': profile,
    }
    return render(request, 'Profile.html', profile_name)
