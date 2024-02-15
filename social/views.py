from django.db import models
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccountContent, Account, OptionsMedia
from .serializers import AccountContentSerializer


class AccountContentAPIView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request):
        user = request.user
        account_id = Account.objects.filter(user=user)

        if account_id:
            platform_filter = [OptionsMedia.FACEBOOK, OptionsMedia.INSTAGRAM, OptionsMedia.TIKTOK]
            account_contents = AccountContent.objects.filter(account__in=account_id,
                                                             account__platform__in=platform_filter)
            total_likes = account_contents.aggregate(total_likes=models.Sum('likes_count'))['total_likes']
            platforms = account_contents.values('account__platform').annotate(total_likes=models.Sum('likes_count'))
            platform_likes = account_contents.values('account__platform', 'likes_count')

            return Response({'total_likes': total_likes,
                             'platform_likes': platform_likes}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'User does not have an associated account social'})
