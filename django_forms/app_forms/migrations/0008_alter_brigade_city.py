# Generated by Django 4.1.4 on 2022-12-07 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0007_alter_brigade_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brigade',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City', to='app_forms.cities'),
        ),
    ]