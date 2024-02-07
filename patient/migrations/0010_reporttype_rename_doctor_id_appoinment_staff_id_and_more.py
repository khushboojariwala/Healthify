# Generated by Django 5.0.1 on 2024-01-31 11:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_alter_payment_installment_paid_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('report_charge', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='appoinment',
            old_name='doctor_id',
            new_name='staff_id',
        ),
        migrations.AlterField(
            model_name='payment_installment',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 11, 17, 15, 307544, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='patient',
            name='report_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='patient.reporttype'),
        ),
    ]
