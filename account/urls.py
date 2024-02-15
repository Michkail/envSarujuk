from django.urls import path
from .views import logging, logging_out, profile_detail

urlpatterns = [
    path('login/', logging, name='login'),
    path('log-out/', logging_out, name='log-out'),
    path('profile/', profile_detail, name='profile'),
]
