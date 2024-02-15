from rest_framework import serializers
from .models import AccountContent


class AccountContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountContent
        fields = '__all__'
