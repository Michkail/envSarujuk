from django.contrib import admin
from .models import User
from social.models import Address


class AddressInline(admin.TabularInline):
    model = Address
    fields = ('province', 'postal_code', 'address_detail')
    readonly_fields = fields
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ('email', 'username', 'get_address')

    def get_address(self, obj):
        if obj.address_id:
            address = obj.address_id
            return f'{address.province} - {address.postal_code} - {address.address_detail}'
        return '-'

    get_address.short_description = 'Address'


admin.site.register(User, UserAdmin)
