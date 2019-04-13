from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class Dzial(models.Model):
  name = models.CharField(max_length=25, null=False, blank=False)
  department_code = models.CharField(max_length=5, null=False, blank=False)
  def __str__(self):
    return self.name + "(" + self.department_code + ")"

class Pracownik(models.Model):
  dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=15)
  last_name = models.CharField(max_length=25)
  phone_number = PhoneNumberField(null=False, blank=False, unique=True)
  email = models.EmailField(max_length=125)
  position = models.CharField(max_length=50)

  def __str__(self):
    return self.first_name + ' ' + self.last_name
