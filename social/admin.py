from django.contrib import admin
from .models import SocialMedia, Platform, Account, AccountContent, CommentParent, Comment, Media
from account.models import User


class PlatformInline(admin.TabularInline):
    model = Platform
    fields = ('name',)
    extra = 0
    exclude = ('platform_id', 'account_id')


class SocialMediaAdmin(admin.ModelAdmin):
    model = SocialMedia
    exclude = ('social_media_id', 'platform_id')


class PlatformAdmin(admin.ModelAdmin):
    model = Platform
    exclude = ('platform_id', 'account_id')


# admin.site.register(SocialMediaAdmin)
admin.site.register(Platform, PlatformAdmin)
