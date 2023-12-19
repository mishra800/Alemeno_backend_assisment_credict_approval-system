# Generated by Django 5.0 on 2023-12-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='current_debt',
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(default=18),
            preserve_default=False,
        ),
    ]