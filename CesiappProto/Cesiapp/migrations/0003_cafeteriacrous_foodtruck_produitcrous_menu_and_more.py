# Generated by Django 4.2.11 on 2024-05-22 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cesiapp', '0002_alter_parking_p_places_alter_type_place_t_nb_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafeteriaCrous',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Cafeteria Crous',
                'verbose_name_plural': 'Cafeterias Crous',
            },
        ),
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('menu', models.TextField(max_length=500)),
                ('contact', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Food Truck',
                'verbose_name_plural': 'Food Trucks',
            },
        ),
        migrations.CreateModel(
            name='ProduitCrous',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('produit_name', models.CharField(max_length=15)),
                ('price', models.IntegerField(default=0)),
                ('in_stock', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Produit Crous',
                'verbose_name_plural': 'Produits Crous',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('food_la', models.BooleanField(default=True)),
                ('crous_la', models.BooleanField(default=True)),
                ('cafeteria_crous', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='Cesiapp.cafeteriacrous')),
                ('food_truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='Cesiapp.foodtruck')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.AddField(
            model_name='cafeteriacrous',
            name='menu',
            field=models.ManyToManyField(to='Cesiapp.produitcrous'),
        ),
    ]
