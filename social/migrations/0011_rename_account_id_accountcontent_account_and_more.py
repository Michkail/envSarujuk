# Generated by Django 5.0.1 on 2024-02-08 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_rename_description_accountcontent_caption_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountcontent',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='accountcontent',
            old_name='address_id',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='accountcontent',
            old_name='comment_parent_id',
            new_name='comment_parent',
        ),
        migrations.RenameField(
            model_name='accountcontent',
            old_name='media_id',
            new_name='media',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_parent_id',
            new_name='comment_parent',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='media_location',
            new_name='media_path',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='socialmedia',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='socialmedia',
            old_name='platform_id',
            new_name='platform',
        ),
    ]
