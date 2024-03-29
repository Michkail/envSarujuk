# Generated by Django 5.0.1 on 2024-02-05 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_user_photo_profile'),
        ('social', '0008_socialmedia_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='social_media_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_society', to='social.socialmedia'),
        ),
    ]
