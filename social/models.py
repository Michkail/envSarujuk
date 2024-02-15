import uuid

from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
# from django.contrib.gis.db import models as geo
from django.db import models
from django.utils.text import gettext_lazy as _


# Create your models here.
class OptionsMedia(models.TextChoices):
    X = "X"
    FACEBOOK = "Facebook"
    INSTAGRAM = "Instagram"
    GOOGLE_MAPS = "Google Maps"
    TIKTOK = "Tiktok"


class OptionsProvince(models.TextChoices):
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
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    province = models.CharField(max_length=100, choices=OptionsProvince.choices, default=OptionsProvince.JAKARTA,
                                blank=True, null=True)
    account_content = models.ForeignKey('AccountContent', on_delete=models.CASCADE, blank=True, null=True)
    postal_code = models.CharField(max_length=5,
                                   validators=[RegexValidator('^[0-9]{5}$', _('Invalid postal code'))],
                                   blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    # location = geo.PointField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return ""


class Account(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, blank=True, null=True)
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    platform = models.CharField(max_length=20, choices=OptionsMedia.choices, default=OptionsMedia.X)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    followers = models.PositiveIntegerField(null=True, blank=True)
    following = models.PositiveIntegerField(null=True, blank=True)
    likes_count = models.PositiveIntegerField(null=True, blank=True)
    posts_count = models.PositiveIntegerField(null=True, blank=True)
    friends = models.PositiveIntegerField(null=True, blank=True)
    reviews = models.PositiveIntegerField(null=True, blank=True)
    tweets = models.PositiveIntegerField(null=True, blank=True)
    photo_profile = models.ImageField(upload_to='photos/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return (f'{self.name if self.name is not None else "Name must be filled"} - '
                f'username ({self.username if self.username is not None else "username is not filled"}) '
                f' - Platform ({self.platform})')


class AccountContent(models.Model):
    account_content_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True)
    caption = models.TextField()
    media = models.ManyToManyField('Media', blank=True)
    content_code = models.CharField(max_length=40, blank=True, null=True, unique=True)
    media_count = models.PositiveIntegerField(null=True, blank=True)
    likes_count = models.PositiveIntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.content_code


class CommentParent(models.Model):
    comment_parent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_detail = models.TextField()
    content_code = models.ForeignKey('AccountContent', on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment_detail


class Comment(models.Model):
    comment_parent = models.ForeignKey('CommentParent', on_delete=models.CASCADE, null=True)
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_detail = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment_detail

#
# def media_upload_path(instance, filename):
#     user_name = instance.user.name if instance.user else 'unknown_user'
#     platform_name = instance.platform.name if instance.platform else 'unknown_platform'
#     return os.path.join('media_files', user_name, platform_name, filename)


class Media(models.Model):
    media_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True)
    # user = models.ForeignKey(acc_user.User, on_delete=models.CASCADE, related_name='media', null=True, blank=True)
    # platform = models.ForeignKey('Platform', on_delete=models.CASCADE, related_name='media', null=True, blank=True)
    # media_location = models.FileField(upload_to=media_upload_path)
    media_path = models.FileField(upload_to='media/social/')
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)


class Statistic(models.Model):
    dash_data_one = ArrayField(ArrayField(models.IntegerField()))
