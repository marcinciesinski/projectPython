from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Dzial(models.Model):
  name = models.CharField(max_length=25)
  department_code = models.CharField(max_length=5)

class Pracownik(models.Model):
  dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=15)
  last_name = models.CharField(max_length=25)
  phone_number = PhoneNumberField(null=False, blank=False, unique=True)
  email = models.EmailField()
  position = models.CharField(max_lenght=50)
