# Generated by Django 5.0.1 on 2024-02-06 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_socialmedia_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='account_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.account'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(blank=True, choices=[('X', 'X'), ('Facebook', 'Fb'), ('Instagram', 'Ig'), ('Google Maps', 'Gm'), ('Tiktok', 'Tt')], default='X', max_length=100, null=True),
        ),
    ]