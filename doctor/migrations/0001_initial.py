# Generated by Django 5.0 on 2024-01-25 08:18

import master.utils.generate_unique_id
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ImageField(default='default_images\\doctor-profile.png', upload_to=master.utils.generate_unique_id.custom_filename)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=255)),
                ('total_patient', models.IntegerField(default=0)),
                ('summary', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]