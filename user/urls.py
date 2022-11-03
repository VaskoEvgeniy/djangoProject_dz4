"""User App URL Configuration"""

from django.urls import path
from user.views import homepage_views
from user.views import u_profile


urlpatterns = [
    path('homepage/<str:username>/', homepage_views, name='user_profile'),
    path('profile/<str:profile>/', u_profile, name='profile'),
]