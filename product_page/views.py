from django.shortcuts import render
from django.http import HttpRequest, HttpResponse




def product_p(request: HttpRequest, product) -> HttpResponse:
    pr_page = {
    'name_shop' : product,
    'username' : 'anonim_user'
    }
    return render(request, 'product_page.html', pr_page)