# Generated by Django 5.0.1 on 2024-02-10 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_media_account_alter_account_platform_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountcontent',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='account_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.accountcontent'),
        ),
    ]
