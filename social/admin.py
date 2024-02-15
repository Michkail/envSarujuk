from django.contrib import admin
from .models import Account, AccountContent, Address, CommentParent, Comment, Media, Statistic


class AccountInline(admin.TabularInline):
    model = Account
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class CommentParentInline(admin.TabularInline):
    model = CommentParent
    extra = 0


class CommentChildInline(admin.TabularInline):
    model = Comment
    extra = 0


class AccountAdmin(admin.ModelAdmin):
    inline = [AddressInline]
    list_display = ['user', 'platform', 'username', 'name']


class AccountContentAdmin(admin.ModelAdmin):
    inlines = [CommentParentInline, AddressInline]
    list_display = ['account', 'content_code']
    search_fields = ['content_code',]


class CommentParentAdmin(admin.ModelAdmin):
    inlines = [CommentChildInline]


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountContent, AccountContentAdmin)
admin.site.register(CommentParent, CommentParentAdmin)
admin.site.register(Comment)
admin.site.register(Media)
admin.site.register(Statistic)
