# Generated by Django 5.0.1 on 2024-01-31 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_remove_patient_report_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_installment',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 11, 3, 23, 493585, tzinfo=datetime.timezone.utc)),
        ),
    ]
