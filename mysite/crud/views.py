from django.shortcuts import render, get_object_or_404

from .models import Dzial, Pracownik

def index(request):
  return render(request, 'crud/index.html')

def dzialy(request):
  dzial_list = Dzial.objects.all().order_by('pk')
  context = {'dzial_list': dzial_list}
  return render(request, 'crud/dzialy.html', context)

def dzial_details(request, dzial_id):
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  context = {'dzial': dzial}
  return render(request, 'crud/dzialDetails.html', context)
