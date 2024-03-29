# Generated by Django 5.0.1 on 2024-02-10 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_remove_accountcontent_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountcontent',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='accountcontent',
            name='comment_parent',
        ),
        migrations.AddField(
            model_name='commentparent',
            name='account_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.accountcontent'),
        ),
    ]
