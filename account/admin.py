from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from .models import User as iUser
from social.models import Address


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
    inlines = [AddressInline]
    actions = ['reset-passwords']
    list_display = ('email', 'username')
    readonly_fields = ('date_updated', 'date_joined')
    exclude = ('social_media_id', 'address_id')
    add_fieldsets = (None, {'classes': ('wide',),
                            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'is_client',
                                       'is_staff', 'is_superuser')}),

    def get_address(self, obj):
        address = obj.address_id
        return f'{address.address_id == ""} - {address.province} - {address.postal_code} - {address.address}'

    get_address.short_description = 'Address'

    #
    # def reset_passwords(self, request, queryset):
    #     for user in queryset:
    #         new_pass = User.objects.make_random_password()
    #         user.set_password(new_pass)
    #         user.save()
    #         messages.success(request,
    #                          f"Password reset successfully for {user.username}. New password: {new_pass}")
    #
    # reset_passwords.short_description = "Reset password for selected users"


admin.site.register(iUser, UserAdmin)
