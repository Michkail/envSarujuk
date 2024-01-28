from django.urls import path
from .views import logging, logging_out

urlpatterns = [
    path('login/', logging, name='login'),
    path('log-out/', logging_out, name='log-out')
]
