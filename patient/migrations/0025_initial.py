# Generated by Django 5.0.1 on 2024-02-05 14:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0003_initial'),
        ('patient', '0024_remove_patient_doctor_id_remove_patient_report_type_and_more'),
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
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('total_amount', models.FloatField(blank=True)),
                ('paid_amount', models.FloatField(default=0)),
                ('remaining_amount', models.FloatField(blank=True)),
                ('payment_status', models.CharField(default='Pending', max_length=255)),
                ('address', models.TextField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.reporttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='payment_installment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('paid_date', models.DateField(default=django.utils.timezone.now)),
                ('paid_payment', models.FloatField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
