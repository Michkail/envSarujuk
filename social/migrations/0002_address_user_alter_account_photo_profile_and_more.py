# Generated by Django 5.0.1 on 2024-01-12 18:15

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='account',
            name='photo_profile',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='accountcontent',
            name='account_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.account'),
        ),
        migrations.AlterField(
            model_name='accountcontent',
            name='address_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.address'),
        ),
        migrations.AlterField(
            model_name='accountcontent',
            name='comment_parent_id',
            field=models.ManyToManyField(blank=True, to='social.commentparent'),
        ),
        migrations.AlterField(
            model_name='accountcontent',
            name='media_id',
            field=models.ManyToManyField(blank=True, to='social.media'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{5}$', 'Invalid postal code')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(blank=True, choices=[('Nanggroe Aceh Darussalam', 'Nanggroe Aceh Darussalam'), ('Sumatera Utara', 'Sumatera Utara'), ('Sumatera Selatan', 'Sumatera Selatan'), ('Sumatera Barat', 'Sumatera Barat'), ('Bengkulu', 'Bengkulu'), ('Riau', 'Riau'), ('Kepulauan Riau', 'Kepulauan Riau'), ('Jambi', 'Jambi'), ('Lampung', 'Lampung'), ('Bangka Belitung', 'Bangka Belitung'), ('Kalimantan Barat', 'Kalimantan Barat'), ('Kalimantan Timur', 'Kalimantan Timur'), ('Kalimantan Selatan', 'Kalimantan Selatan'), ('Kalimantan Tengah', 'Kalimantan Tengah'), ('Kalimantan Utara', 'Kalimantan Utara'), ('Banten', 'Banten'), ('Jakarta', 'Jakarta'), ('Jawa Barat', 'Jawa Barat'), ('Jawa Tengah', 'Jawa Tengah'), ('Yogyakarta', 'Yogyakarta'), ('Jawa Timur', 'Jawa Timur'), ('Bali', 'Bali'), ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'), ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'), ('Gorontalo', 'Gorontalo'), ('Sulawesi Barat', 'Sulawesi Barat'), ('Sulawesi Tengah', 'Sulawesi Tengah'), ('Sulawesi Utara', 'Sulawesi Utara'), ('Sulawesi Tenggara', 'Sulawesi Tenggara'), ('Sulawesi Selatan', 'Sulawesi Selatan'), ('Maluku Utara', 'Maluku Utara'), ('Maluku', 'Maluku'), ('Papua Barat', 'Papua Barat'), ('Papua', 'Papua'), ('Papua Tengah', 'Papua Tengah'), ('Papua Pengungan', 'Papua Pegunungan'), ('Papua Selatan', 'Papua Selatan'), ('Papua Barat Daya', 'Papua Barat Daya')], default='Jakarta', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='account_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.account'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
