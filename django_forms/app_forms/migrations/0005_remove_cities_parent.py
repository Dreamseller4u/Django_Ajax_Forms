# Generated by Django 4.1.4 on 2022-12-07 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0004_rename_parnet_cities_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='parent',
        ),
    ]
