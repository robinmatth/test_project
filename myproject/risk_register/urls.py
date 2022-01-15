from django.urls import path

from . import views
from risk_register.views import index

urlpatterns = [
    path('risk_register', views.risk_register, name='risk_register'),
    path('export_csv', views.export_csv, name='export-csv'),


]