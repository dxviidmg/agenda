from django.db import models
from django.contrib.auth.models import User
import re

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

    def __str__(self):
        return self.number

class Email(models.Model):
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    email = models.EmailField(max_length=15)

    def __str__(self):
        return self.email

class Address(models.Model):
    type_choices = (
        ('Personal', 'Personal'),
        ('Work', 'Work'),
    )

    contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    street = models.CharField(max_length=15)
    outdoor_Number = models.CharField(max_length=15)
    location = models.CharField(max_length=20) #Colonia
    city = models.CharField(max_length=15)
    province = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    CP = models.CharField(max_length=5)
    type_address = models.CharField(max_length=10, choices=type_choices, default='Personal')

    def concatenate(self):
        
        c = ' '.join([self.street, self.outdoor_Number, self.location,  self.city, self.province, self.country])
        c = c.replace(',', '')
        c = re.sub(' +', ' ', c)
        return c
    
    def __str__(self):
        return self.concatenate()

