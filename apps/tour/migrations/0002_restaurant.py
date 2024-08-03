# Generated by Django 5.0.7 on 2024-08-03 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='restaurnats/')),
                ('adress', models.CharField(max_length=500)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='tour.country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]