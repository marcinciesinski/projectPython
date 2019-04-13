from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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

