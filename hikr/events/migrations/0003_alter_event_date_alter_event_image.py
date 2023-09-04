# Generated by Django 4.2.4 on 2023-09-04 14:11

import datetime
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 17, 11, 44, 238413)),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='events/images/default.png', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[768, 1024], upload_to='events/images'),
        ),
    ]
