# Generated by Django 5.0.1 on 2024-02-05 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0021_remove_payment_installment_appoinment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctor'),
        ),
    ]