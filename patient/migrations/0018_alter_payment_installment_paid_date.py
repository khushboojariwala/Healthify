# Generated by Django 5.0.1 on 2024-02-02 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0017_alter_payment_installment_paid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_installment',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 2, 7, 13, 4, 886814, tzinfo=datetime.timezone.utc)),
        ),
    ]
