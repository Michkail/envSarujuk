from django.urls import path
from .views import AccountContentAPIView

urlpatterns = [
    path('likes_count/', AccountContentAPIView.as_view(), name='account-content-api')
]
