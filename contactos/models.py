from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
Ejercicio: Una agenda donde se puedan dar de alta contactos, cada contacto tiene telefonos, emails y direcciones. 

"""

class Contact(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    def get_full_name(self):
        return self.name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

    

class Phone(models.Model):
    type_choices = (
        ('Celular', 'Celular'),
        ('House', 'House'),
    )
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    number = models.CharField(max_length=15)
    type_phone = models.CharField(max_length=10, choices=type_choices, default='Celular')


class Email(models.Model):
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    email = models.EmailField(max_length=15)


class Address(models.Model):
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    street = models.CharField(max_length=15)
    num_ext = models.CharField(max_length=15)
    num_int = models.CharField(max_length=15)
    location = models.CharField(max_length=20) #Colonia
    city = models.CharField(max_length=15)
    province = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    CP = models.CharField(max_length=5)

    

