# Generated by Django 5.0.7 on 2024-08-01 10:33

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/countries/')),
            ],
            options={
                'verbose_name': 'Davlat',
                'verbose_name_plural': 'Davlatlar',
            },
        ),
        migrations.CreateModel(
            name='HotelFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/destinations/')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.country')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('stars', models.PositiveSmallIntegerField(default=1)),
                ('image', models.ImageField(upload_to='hotels/')),
                ('address', models.CharField(max_length=100)),
                ('hotel_class', models.CharField(blank=True, max_length=100, null=True)),
                ('images', models.ManyToManyField(blank=True, to='main.image')),
                ('facilities', models.ManyToManyField(blank=True, to='tour.hotelfacility')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images/tours/')),
                ('hit_count', models.PositiveIntegerField(default=0)),
                ('price_list', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('programm', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('visa', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('categories', models.ManyToManyField(blank=True, to='tour.category')),
                ('countries', models.ManyToManyField(blank=True, to='tour.country')),
                ('destinations', models.ManyToManyField(blank=True, related_name='tours', to='tour.destination')),
                ('hotels', models.ManyToManyField(blank=True, to='tour.hotel')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('has_breakfast', models.BooleanField(default=True)),
                ('has_lunch', models.BooleanField(default=False)),
                ('has_dinner', models.BooleanField(default=False)),
                ('breakfast', models.TextField(blank=True, null=True)),
                ('lunch', models.TextField(blank=True, null=True)),
                ('dinner', models.TextField(blank=True, null=True)),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='tour.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.PositiveSmallIntegerField(default=1)),
                ('body', models.TextField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tour.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
