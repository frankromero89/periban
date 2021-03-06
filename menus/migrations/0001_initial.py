# Generated by Django 3.2.8 on 2021-11-11 04:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Comidas', max_length=50)),
                ('image', models.ImageField(upload_to='menus/images')),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='nombre', max_length=50)),
                ('url_name', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='descripción')),
                ('costo', models.DecimalField(decimal_places=2, default='1.00', max_digits=6)),
                ('little_image', models.ImageField(upload_to='menus/images/platillos')),
                ('big_image', models.ImageField(upload_to='menus/images/platillos')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu')),
            ],
        ),
    ]
