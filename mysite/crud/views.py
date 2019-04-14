from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    dzial_to_add = Dzial(name = request.POST['departmentName'], department_code = request.POST['departmentCode'])
    if dzial_to_add.name != "" or dzial_to_add.department_code != "":
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
    dzial_to_change = get_object_or_404(Dzial, pk = dzial_id)
    dzial_to_change.name = request.POST['departmentName']
    dzial_to_change.department_code = request.POST['departmentCode']
    if dzial_to_change.name != "" or dzial_to_change.department_code != "":
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

def prac_add(request, dzial_id):
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  return render (request, 'crud/pracAdd.html',{'dzial': dzial})

def dzial_add_new_prac(request, dzial_id):
  if request.method == 'POST':
    dzial = get_object_or_404(Dzial, pk = dzial_id)
    prac_to_add = dzial.pracownik_set.create(
                              first_name = request.POST['pracownikName'],
                              last_name = request.POST['pracownikLastName'],
                              phone_number = request.POST['pracownikPhoneNum'],
                              email = request.POST['pracownikEmail'],
                              position = request.POST['pracownikPosition'])
    
    prac_to_add.save()
    return HttpResponseRedirect(reverse('crud:dzial_details', args=[dzial_id]))
  else:
    return render(request, 'crud/pracAdd.html',{'error_message_add': "Coś poszło nie tak... spróbuj ponownie."})

def prac_edit(request, dzial_id, prac_id):
  dzial = get_object_or_404(Dzial, pk = dzial_id)
  prac = dzial.pracownik_set.get(pk = prac_id)
  context = {'dzial': dzial, 'prac': prac}
  return render(request, 'crud/pracEdit.html', context)

def prac_to_edit(request, dzial_id, prac_id):
  if request.method == 'POST':
    prac_to_edit = get_object_or_404(Pracownik, pk = prac_id)
    prac_to_edit.dzial = request.POST['dzialId']
    prac_to_edit.first_name = request.POST['pracownikName']
    prac_to_edit.last_name = request.POST['pracownikLastName']
    prac_to_edit.phone_number = request.POST['pracownikPhoneNum']
    prac_to_edit.email = request.POST['pracownikEmail']
    prac_to_edit.position = request.POST['pracownikPosition']
    prac_to_edit.save()
    return HttpResponseRedirect(reverse('crud:dzial_details', args=[dzial_id]))



