from django.urls import path
from product_page.views import product_p

urlpatterns = [
    path('<str:product>/', product_p, name='product')
]