# Generated by Django 5.0.1 on 2024-01-31 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_alter_patient_report_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_installment',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 10, 59, 27, 452321, tzinfo=datetime.timezone.utc)),
        ),
    ]