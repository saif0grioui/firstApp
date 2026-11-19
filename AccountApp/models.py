from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    pass

number_validator = RegexValidator(r'^\d{8}$', message="Le Numéro doit contenir exactement 8 chiffres.")

def birth_date_validator(d):
    if d >= timezone.localdate():
        raise ValidationError("La date de naissance doit être antérieur que la date d.")

class Doctor(models.Model):
    license_number = models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone = models.CharField(max_length=8, validators=[number_validator])
    Specialty = models.ManyToManyField("AccountApp.Specialty", related_name='Doctors')

    
class Patient(models.Model):
    national_id = models.CharField(max_length=8,unique=True,validators=[number_validator])
    phone = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField(validators=[birth_date_validator])

class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)