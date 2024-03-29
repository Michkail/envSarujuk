# Generated by Django 5.0.1 on 2024-01-08 06:13

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "account_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("username", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=255)),
                ("photo_profile", models.ImageField(upload_to="photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "address_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "province",
                    models.CharField(
                        choices=[
                            ("Nanggroe Aceh Darussalam", "Nanggroe Aceh Darussalam"),
                            ("Sumatera Utara", "Sumatera Utara"),
                            ("Sumatera Selatan", "Sumatera Selatan"),
                            ("Sumatera Barat", "Sumatera Barat"),
                            ("Bengkulu", "Bengkulu"),
                            ("Riau", "Riau"),
                            ("Kepulauan Riau", "Kepulauan Riau"),
                            ("Jambi", "Jambi"),
                            ("Lampung", "Lampung"),
                            ("Bangka Belitung", "Bangka Belitung"),
                            ("Kalimantan Barat", "Kalimantan Barat"),
                            ("Kalimantan Timur", "Kalimantan Timur"),
                            ("Kalimantan Selatan", "Kalimantan Selatan"),
                            ("Kalimantan Tengah", "Kalimantan Tengah"),
                            ("Kalimantan Utara", "Kalimantan Utara"),
                            ("Banten", "Banten"),
                            ("Jakarta", "Jakarta"),
                            ("Jawa Barat", "Jawa Barat"),
                            ("Jawa Tengah", "Jawa Tengah"),
                            ("Yogyakarta", "Yogyakarta"),
                            ("Jawa Timur", "Jawa Timur"),
                            ("Bali", "Bali"),
                            ("Nusa Tenggara Timur", "Nusa Tenggara Timur"),
                            ("Nusa Tenggara Barat", "Nusa Tenggara Barat"),
                            ("Gorontalo", "Gorontalo"),
                            ("Sulawesi Barat", "Sulawesi Barat"),
                            ("Sulawesi Tengah", "Sulawesi Tengah"),
                            ("Sulawesi Utara", "Sulawesi Utara"),
                            ("Sulawesi Tenggara", "Sulawesi Tenggara"),
                            ("Sulawesi Selatan", "Sulawesi Selatan"),
                            ("Maluku Utara", "Maluku Utara"),
                            ("Maluku", "Maluku"),
                            ("Papua Barat", "Papua Barat"),
                            ("Papua", "Papua"),
                            ("Papua Tengah", "Papua Tengah"),
                            ("Papua Pengungan", "Papua Pegunungan"),
                            ("Papua Selatan", "Papua Selatan"),
                            ("Papua Barat Daya", "Papua Barat Daya"),
                        ],
                        default="Jakarta",
                        max_length=100,
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        max_length=5,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]{5}$", "Invalid postal code"
                            )
                        ],
                    ),
                ),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CommentParent",
            fields=[
                (
                    "comment_parent_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("comment_detail", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "media_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("media_location", models.FileField(upload_to="media/social/")),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "comment_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("comment_detail", models.TextField()),
                (
                    "comment_parent_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="social.commentparent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AccountContent",
            fields=[
                (
                    "account_content_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField()),
                ("media_count", models.IntegerField()),
                ("comment_count", models.IntegerField()),
                (
                    "account_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="social.account"
                    ),
                ),
                (
                    "address_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="social.address"
                    ),
                ),
                (
                    "comment_parent_id",
                    models.ManyToManyField(to="social.commentparent"),
                ),
                ("media_id", models.ManyToManyField(to="social.media")),
            ],
        ),
        migrations.CreateModel(
            name="Platform",
            fields=[
                (
                    "platform_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "account_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="social.account"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialMedia",
            fields=[
                (
                    "social_media_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "platform_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="social.platform",
                    ),
                ),
            ],
        ),
    ]
