from django.contrib import admin
from .models import User
from social.models import Address


class AddressInline(admin.TabularInline):
    model = Address
    fields = ('province', 'postal_code', 'address')
    extra = 0
    exclude = ('address_id',)


class UserAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ('email', 'username')
    exclude = ('social_media_id', 'address_id')

    def get_address(self, obj):
        address = obj.address_id
        return f'{address.address_id == ""} - {address.province} - {address.postal_code} - {address.address}'

    get_address.short_description = 'Address'


admin.site.register(User, UserAdmin)
