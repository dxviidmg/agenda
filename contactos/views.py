from django.shortcuts import render
from contactos.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ContactsListView(ListView):
	model = Contact


class ContactDetailView(DetailView):
	model = Contact

	def get_context_data(self, **kwargs):
		context = super(ContactDetailView, self).get_context_data(**kwargs)
		context['phones'] = Phone.objects.filter(contact=self.object)
		context['emails'] = Email.objects.filter(contact=self.object)
		context['adresses'] = Address.objects.filter(contact=self.object)

#		print(context)
		return context