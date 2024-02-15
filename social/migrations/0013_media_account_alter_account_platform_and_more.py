# Generated by Django 5.0.1 on 2024-02-08 20:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_remove_socialmedia_platform_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='platform',
            field=models.CharField(choices=[('X', 'X'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Google Maps', 'Google Maps'), ('Tiktok', 'Tiktok')], default='X', max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]