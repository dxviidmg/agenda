from django.urls import path
from .views import *

app_name = 'contacts'

urlpatterns = [
#	path('escuela/<slug:slug>/', EscuelaDetailView.as_view(), name='escuela-detail'),
#	path('entidad-convocatoria/<slug:slug>/', EntidadConvocatoriaDetailView.as_view(), name='entidad-convocatoria-detail'),
#	path('entidad/<slug:slug>/', EntidadDetailView.as_view(), name='entidad-detail'),
#	path('region/<slug:slug>/', RegionDetailView.as_view(), name='region-detail'),
	path('contacts/', ContactsListView.as_view(), name='contact-list'),
]