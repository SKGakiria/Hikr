# Generated by Django 4.2.4 on 2023-09-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="groupmembership",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
