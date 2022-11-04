# Generated by Django 4.1.2 on 2022-11-04 20:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coach",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("birthdate", models.DateField()),
                ("biography", models.CharField(max_length=500)),
                ("hometown", models.CharField(max_length=50)),
            ],
        ),
    ]
