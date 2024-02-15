from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .models import User as iUser
from social.models import Address, Account


class AccountInline(admin.TabularInline):
    model = Account
    fields = ('posts_count', 'followers', 'following')
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    fields = ('province', 'postal_code', 'address')
    extra = 0
    exclude = ('address_id',)


class AddUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = iUser
        fields = ('username', 'email', 'is_client', 'is_staff', 'is_superuser', 'password')
        exclude = ('password',)


class UserAdmin(BaseUserAdmin):
    inlines = [AddressInline, AccountInline]
    actions = ['reset-passwords']
    list_display = ('username', 'email', 'photo_profile')
    readonly_fields = ('date_updated', 'date_joined')
    exclude = ('social_media_id', 'address_id')
    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'photo_profile', 'phone_number')}),
                 ('Permissions', {'fields': ('is_client', 'is_active', 'is_staff', 'is_superuser')}),
                 ('Important Dates', {'fields': ('last_login', 'date_updated', 'date_joined')}),)
    add_fieldsets = (None, {'classes': ('wide',),
                            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'is_client',
                                       'is_staff', 'is_superuser')}),

    def get_address(self, obj):
        address = obj.address_id

        return f'{address.province} - {address.postal_code} - {address.address}'

    def get_account(self, obj):
        social = obj.account_id

        return f'{social.name}'

    get_address.short_description = 'Address User'
    get_account.short_description = 'Social Media Account'


admin.site.unregister(Group)
admin.site.register(iUser, UserAdmin)
