# Generated by Django 4.1.2 on 2023-11-22 02:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="publication_date",
            field=models.DateTimeField(),
        ),
    ]
