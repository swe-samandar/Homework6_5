# Generated by Django 5.1.6 on 2025-03-01 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.PositiveIntegerField()),
                ('inventory_value', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.phone')),
            ],
            options={
                'verbose_name': 'dealer',
                'ordering': ['-created_at'],
            },
        ),
    ]
