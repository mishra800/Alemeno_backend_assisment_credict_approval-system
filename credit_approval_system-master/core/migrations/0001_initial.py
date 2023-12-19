# Generated by Django 5.0 on 2023-12-17 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.PositiveIntegerField()),
                ('monthly_salary', models.PositiveIntegerField()),
                ('approved_limit', models.PositiveIntegerField()),
                ('current_debt', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_amount', models.FloatField()),
                ('tenure', models.PositiveIntegerField()),
                ('interest_rate', models.FloatField()),
                ('monthly_repayment', models.FloatField()),
                ('emis_paid_on_time', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
        ),
    ]
