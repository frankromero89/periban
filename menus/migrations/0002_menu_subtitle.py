# Generated by Django 3.2.8 on 2021-11-11 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='subtitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
