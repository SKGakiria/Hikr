# Generated by Django 4.2.4 on 2023-08-24 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225, unique=True)),
                ('image', django_resized.forms.ResizedImageField(crop=None, default='groups/images/default.png', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[400, 500], upload_to='groups/images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'groups',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GroupMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='groups.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'group_memberships',
                'ordering': ['-joined_at'],
                'unique_together': {('user', 'group')},
            },
        ),
    ]