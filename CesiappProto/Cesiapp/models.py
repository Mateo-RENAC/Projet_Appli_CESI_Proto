from django.db import models

class Compte(models.Model):
    """
    Table "Compte" sert à identifier le type de l'utilisateur et son moyen de transport
    """
    TYPE_CHOICES = [
        ('Rep_P', 'Rep_P'),
        ('Etud', 'Etud'),
        ('Invit', 'Invit'),
    ]

    PREF_P_CHOICES = [
        ('Elect', 'Elect'),
        ('Therm', 'Therm'),
        ('None', 'None'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    pref_p = models.CharField(max_length=6, choices=PREF_P_CHOICES)

    class Meta:
        verbose_name_plural = 'Compte'
        verbose_name = 'Compte'

    def __str__(self):
        return f"{self.username} ({self.type})"


class Parking(models.Model):
    """
    Table Parking sert à avoir une vue globale des 2 parkings et leurs places disponibles
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=6)
    p_places = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Parking'
        verbose_name = 'Parking'

    def __str__(self):
        return f"{self.name} ({self.p_places} places)"


class Type_Place(models.Model):
    """
    Table Type_Place sert à identifier les types de places dans chaque Parking et le nombre qu'il reste
    """
    TYPE_PLACE_CHOICES = [
        ('Electrique', 'Electrique'),
        ('Thermique', 'Thermique'),
    ]

    id = models.AutoField(primary_key=True)
    fk_id_parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    name_Type = models.CharField(max_length=11, choices=TYPE_PLACE_CHOICES)
    t_nb_places = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Type_Place'
        verbose_name = 'Type_Place'

    def __str__(self):
        return f"{self.name_Type} ({self.t_nb_places} places, Parking: {self.fk_id_parking.name})"


from django.db import models

class ProduitCrous(models.Model):
    id = models.AutoField(primary_key=True)
    produit_name = models.CharField(max_length=15)
    price = models.FloatField(default=0.0)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Produits Crous'
        verbose_name = 'Produit Crous'

    def __str__(self):
        return f"{self.produit_name} ({self.price}€) - Disponible : {'Oui' if self.in_stock else 'Non'}"


class CafeteriaCrous(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ManyToManyField(ProduitCrous)

    class Meta:
        verbose_name_plural = 'Cafeterias Crous'
        verbose_name = 'Cafeteria Crous'

    def __str__(self):
        return ', '.join([str(produit) for produit in self.menu.all()])


class FoodTruck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    menu = models.TextField(max_length=500)
    contact = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Food Trucks'
        verbose_name = 'Food Truck'

    def __str__(self):
        return f"{self.name} ({self.menu} - {self.contact})"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    cafeteria_crous = models.ForeignKey(CafeteriaCrous, on_delete=models.CASCADE, related_name='menus')
    food_truck = models.ForeignKey(FoodTruck, on_delete=models.CASCADE, related_name='menus')
    date = models.DateField(auto_now_add=True)
    food_la = models.BooleanField(default=True)
    crous_la = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Menus'
        verbose_name = 'Menu'

    def __str__(self):
        return f"Menu du {self.date}"





#Import for signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

#Signals for Automation


@receiver(post_save, sender=Type_Place)
def update_parking_places_on_save(sender, instance, **kwargs):
    update_parking_places(instance.fk_id_parking)


def update_parking_places(parking):
    total_places = Type_Place.objects.filter(fk_id_parking=parking).aggregate(total=Sum('t_nb_places'))['total'] or 0
    parking.p_places = total_places
    parking.save()