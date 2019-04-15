from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import dzialForm, pracForm

from .models import Dzial, Pracownik

  # Metody wyświetlające zawartosc

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

  # Metody CRUD do modelu Dzial

def dzial_delete(request, dzial_id):
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  context = {'dzial': dzial}
  dzial.delete()
  return render(request, 'crud/dzialDelete.html', context)

def dzial_add(request):
  return render(request, 'crud/dzialAdd.html')

def dzial_add_new(request):
  if request.method == 'POST':
    form = dzialForm(request.POST)
    if form.is_valid():
      dzial_to_add = Dzial(name = request.POST['name'], department_code = request.POST['department_code'])
      dzial_to_add.save()
      return HttpResponseRedirect(reverse('crud:dzialy'))
    else:
      return render(request, 'crud/dzialy.html',{'error_message': "Coś poszło nie tak... spróbuj ponownie."})
  else:
    return render(request, 'crud/dzialy.html',{'error_message': "Coś poszło nie tak... spróbuj ponownie."})

def dzial_edit(request, dzial_id):
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  context = {'dzial': dzial}
  return render(request, 'crud/dzialEdit.html', context)

def dzial_to_edit(request, dzial_id):
  if request.method == 'POST':
    form = dzialForm(request.POST)
    if form.is_valid():
      dzial_to_change = get_object_or_404(Dzial, pk = dzial_id)
      dzial_to_change.name = request.POST['name']
      dzial_to_change.department_code = request.POST['department_code']
      dzial_to_change.save()
      return HttpResponseRedirect(reverse('crud:dzialy'))
    else:
      return render(request, 'crud/dzialy.html',{'error_message_edit': "Coś poszło nie tak... spróbuj ponownie."})
  else:
    return render(request, 'crud/dzialy.html',{'error_message_edit': "Coś poszło nie tak... spróbuj ponownie."})

  # METODY CRUD do modelu Pracownik

def prac_delete(request, prac_id, dzial_id):
  prac = get_object_or_404(Pracownik, pk = prac_id)
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  context = {'prac': prac, 'dzial': dzial}
  prac.delete()
  return render(request, 'crud/pracDelete.html', context)

def dzial_add_new_prac(request, dzial_id):
  if request.method == 'POST':
    dzial = get_object_or_404(Dzial, pk = dzial_id)
    form = pracForm(request.POST)
    if form.is_valid():
      prac_to_add = dzial.pracownik_set.create(
                                first_name = request.POST['first_name'],
                                last_name = request.POST['last_name'],
                                phone_number = request.POST['phone_number'],
                                email = request.POST['email'],
                                position = request.POST['position'])
      
      prac_to_add.save()
      return HttpResponseRedirect(reverse('crud:dzial_details', args=[dzial_id]))
    else:
      return render(request, 'crud/pracAdd.html',{'error_message_add': "Coś poszło nie tak... spróbuj ponownie.", 'dzial': dzial})
  else:
    return render(request, 'crud/pracAdd.html',{'error_message_add': "Coś poszło nie tak... spróbuj ponownie.", 'dzial': dzial})

def prac_add(request, dzial_id):
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  return render (request, 'crud/pracAdd.html',{'dzial': dzial})

def prac_edit(request, dzial_id, prac_id):
  dzial_list = Dzial.objects.all().order_by('pk')
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  prac = dzial.pracownik_set.get(pk = prac_id)
  context = {'dzial': dzial, 'prac': prac, 'dzial_list':dzial_list}
  return render(request, 'crud/pracEdit.html', context)

def prac_to_edit(request, dzial_id, prac_id):
  if request.method == 'POST':
    print (request.POST)
    form = pracForm(request.POST)
    return_dzial = get_object_or_404(Dzial, pk = dzial_id)
    dzial_to_push = get_object_or_404(Dzial, pk = request.POST['dzial'])
    if form.is_valid():
      prac_to_edit = get_object_or_404(Pracownik, pk = prac_id)
      prac_to_edit.dzial = dzial_to_push
      prac_to_edit.first_name = request.POST['first_name']
      prac_to_edit.last_name = request.POST['last_name']
      prac_to_edit.phone_number = request.POST['phone_number']
      prac_to_edit.email = request.POST['email']
      prac_to_edit.position = request.POST['position']
      prac_to_edit.save()
      return HttpResponseRedirect(reverse('crud:dzial_details', args=[dzial_id]))
    else:
      return render(request, 'crud/pracEdit.html',{'error_message_edit': "Coś poszło nie tak... spróbuj ponownie.", 'dzial': return_dzial})
  else:
    return render(request, 'crud/pracEdit.html',{'error_message_edit': "Coś poszło nie tak... spróbuj ponownie.", 'dzial': return_dzial})




