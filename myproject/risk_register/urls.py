from django.urls import path

from . import views
from risk_register.views import base

urlpatterns = [
    # ex: /index path using base.html
    path('', views.base, name='base'),
    path('export_csv', views.export_csv, name='export-csv'),



    
]