# Generated by Django 5.0.1 on 2024-01-31 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_payment_installment_paid_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='report_type',
        ),
        migrations.AlterField(
            model_name='payment_installment',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 11, 1, 10, 693793, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='ReportType',
        ),
    ]
