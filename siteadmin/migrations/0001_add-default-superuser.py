# Generated by Django 2.0.7 on 2019-01-08 06:18

from django.db import migrations


def add_default_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    from django.contrib.auth.hashers import make_password
    User.objects.create(
        username='superadmin',
        password=make_password('admin'),
        first_name='admin',
        last_name='admin',
        email='admin@demo.com',
        is_staff=True,
        is_superuser=True,
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(add_default_superuser)
    ]
