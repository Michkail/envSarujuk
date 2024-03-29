# Generated by Django 5.0.1 on 2024-02-08 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_user_social_media_id'),
        ('social', '0011_rename_account_id_accountcontent_account_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmedia',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='account',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='platform',
            field=models.CharField(blank=True, choices=[('X', 'X'), ('Facebook', 'Fb'), ('Instagram', 'Ig'), ('Google Maps', 'Gm'), ('Tiktok', 'Tt')], default='X', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Platform',
        ),
        migrations.DeleteModel(
            name='SocialMedia',
        ),
    ]
