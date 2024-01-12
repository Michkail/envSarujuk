import os
import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
class Province(models.TextChoices):
    NANGGROE_ACEH_DARUSSALAM = 'Nanggroe Aceh Darussalam'
    SUMATERA_UTARA = 'Sumatera Utara'
    SUMATERA_SELATAN = 'Sumatera Selatan'
    SUMATERA_BARAT = 'Sumatera Barat'
    BENGKULU = 'Bengkulu'
    RIAU = 'Riau'
    KEPULAUAN_RIAU = 'Kepulauan Riau'
    JAMBI = 'Jambi'
    LAMPUNG = 'Lampung'
    BANGKA_BELITUNG = 'Bangka Belitung'
    KALIMANTAN_BARAT = 'Kalimantan Barat'
    KALIMANTAN_TIMUR = 'Kalimantan Timur'
    KALIMANTAN_SELATAN = 'Kalimantan Selatan'
    KALIMANTAN_TENGAH = 'Kalimantan Tengah'
    KALIMANTAN_UTARA = 'Kalimantan Utara'
    BANTEN = 'Banten'
    JAKARTA = 'Jakarta'
    JAWA_BARAT = 'Jawa Barat'
    JAWA_TENGAH = 'Jawa Tengah'
    YOGYAKARTA = 'Yogyakarta'
    JAWA_TIMUR = 'Jawa Timur'
    BALI = 'Bali'
    NUSA_TENGGARA_TIMUR = 'Nusa Tenggara Timur'
    NUSA_TENGGARA_BARAT = 'Nusa Tenggara Barat'
    GORONTALO = 'Gorontalo'
    SULAWESI_BARAT = 'Sulawesi Barat'
    SULAWESI_TENGAH = 'Sulawesi Tengah'
    SULAWESI_UTARA = 'Sulawesi Utara'
    SULAWESI_TENGGARA = 'Sulawesi Tenggara'
    SULAWESI_SELATAN = 'Sulawesi Selatan'
    MALUKU_UTARA = 'Maluku Utara'
    MALUKU = 'Maluku'
    PAPUA_BARAT = 'Papua Barat'
    PAPUA = 'Papua'
    PAPUA_TENGAH = 'Papua Tengah'
    PAPUA_PEGUNUNGAN = 'Papua Pengungan'
    PAPUA_SELATAN = 'Papua Selatan'
    PAPUA_BARAT_DAYA = 'Papua Barat Daya'


class Address(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, blank=True, null=True)
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    province = models.CharField(max_length=100, choices=Province.choices, default=Province.JAKARTA, blank=True,
                                null=True)
    postal_code = models.CharField(max_length=5,
                                   validators=[RegexValidator('^[0-9]{5}$', _('Invalid postal code'))],
                                   blank=True, null=True)
    address = models.TextField(null=True, blank=True)


class SocialMedia(models.Model):
    social_media_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    platform_id = models.ForeignKey('Platform', on_delete=models.CASCADE)


class Platform(models.Model):
    platform_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)


class Account(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    photo_profile = models.ImageField(upload_to='photos/', blank=True, null=True)


class AccountContent(models.Model):
    account_content_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    media_id = models.ManyToManyField('Media', blank=True)
    media_count = models.IntegerField()
    comment_parent_id = models.ManyToManyField('CommentParent', blank=True)
    comment_count = models.IntegerField()
    address_id = models.ForeignKey('Address', on_delete=models.CASCADE, blank=True, null=True)
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True)


class CommentParent(models.Model):
    comment_parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_detail = models.TextField()


class Comment(models.Model):
    comment_parent_id = models.ForeignKey('CommentParent', on_delete=models.CASCADE, null=True)
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_detail = models.TextField()

#
# def media_upload_path(instance, filename):
#     user_name = instance.user.name if instance.user else 'unknown_user'
#     platform_name = instance.platform.name if instance.platform else 'unknown_platform'
#     return os.path.join('media_files', user_name, platform_name, filename)


class Media(models.Model):
    media_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(acc_user.User, on_delete=models.CASCADE, related_name='media', null=True, blank=True)
    # platform = models.ForeignKey('Platform', on_delete=models.CASCADE, related_name='media', null=True, blank=True)
    # media_location = models.FileField(upload_to=media_upload_path)
    media_location = models.FileField(upload_to='media/social/')
