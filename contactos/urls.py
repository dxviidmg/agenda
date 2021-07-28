from django.urls import path
from .views import *

app_name = 'contacts'

urlpatterns = [
	path('contacts/create/', ContactCreateView.as_view(), name='contact-create'),
	path('contacts/<int:pk>/create-phone/', PhoneCreateView.as_view(), name='phone-create'),
	path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
	path('contacts/', ContactsListView.as_view(), name='contact-list'),
]