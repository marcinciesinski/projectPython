from django.forms import ModelForm
from .models import Dzial, Pracownik

class dzialForm(ModelForm):
  class Meta:
    model = Dzial
    fields = ['name', 'department_code']


class pracForm(ModelForm):
  class Meta:
    model = Pracownik
    fields = ['first_name','last_name', 'phone_number','email','position']