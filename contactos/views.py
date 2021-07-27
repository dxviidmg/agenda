from django.shortcuts import render
from contactos.models import Contact
from django.views.generic.list import ListView


class ContactsListView(ListView):
	model = Contact


