# Generated by Django 5.0 on 2023-12-19 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_loan_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='customer',
            new_name='customer_id',
        ),
    ]
