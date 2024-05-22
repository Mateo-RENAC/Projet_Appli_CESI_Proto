from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Type_Place

def type_place_list(request):
    type_places = Type_Place.objects.select_related('fk_id_parking').all()
    return render(request, 'Cesiapp/ParkingGest.html', {'type_places': type_places})

@require_POST
def update_places(request, pk, action):
    type_place = get_object_or_404(Type_Place, pk=pk)
    if action == 'increment':
        type_place.t_nb_places += 1
    elif action == 'decrement' and type_place.t_nb_places > 0:
        type_place.t_nb_places -= 1
    type_place.save()
    return redirect('type_place_list')
