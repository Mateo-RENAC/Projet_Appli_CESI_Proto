# Generated by Django 4.2.11 on 2024-05-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cesiapp', '0003_cafeteriacrous_foodtruck_produitcrous_menu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitcrous',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
