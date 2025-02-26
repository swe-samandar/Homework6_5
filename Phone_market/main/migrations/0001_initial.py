# Generated by Django 5.1.6 on 2025-02-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('storage_capacity', models.CharField(max_length=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('release_date', models.DateField()),
                ('screen_size', models.CharField(max_length=10)),
                ('battery_capacity', models.PositiveIntegerField()),
                ('processor', models.CharField(max_length=25)),
                ('camera_resolution', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='phone_images/')),
            ],
            options={
                'verbose_name': 'phone',
            },
        ),
    ]
