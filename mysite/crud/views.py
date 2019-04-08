from django.shortcuts import render

from .models import Dzial, Pracownik

def index(request):
  return render(request, 'crud/index.html')

def dzialy(request):
  dzial_list = Dzial.objects.all().order_by('pk')
  context = {'dzial_list': dzial_list}
  return render(request, 'crud/dzialy.html', context)
