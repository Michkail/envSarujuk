# Generated by Django 5.0.1 on 2024-02-08 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_user_social_media_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='social_media_id',
        ),
    ]