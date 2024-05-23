from django.contrib import admin
from .models import Parking, Type_Place, Compte
from .models import ProduitCrous, CafeteriaCrous, FoodTruck, Menu
from .forms import CafeteriaCrousForm
# Register your models here.

admin.site.register(Parking)
admin.site.register(Type_Place)
admin.site.register(Compte)

admin.site.register(ProduitCrous)
admin.site.register(FoodTruck)
admin.site.register(Menu)


class CafeteriaCrousAdmin(admin.ModelAdmin):
    form = CafeteriaCrousForm


admin.site.register(CafeteriaCrous, CafeteriaCrousAdmin)
