from django.shortcuts import render
from .models import Building

# Create your views here.

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'uboapp/building_list.html', {'buildings': buildings})