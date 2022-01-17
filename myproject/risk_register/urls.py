from django.urls import path

from . import views
from risk_register.views import index

urlpatterns = [
    path('risk_register', views.risk_register, name='risk_register'),
    path('add_risks', views.add_risks, name='add_risks'),
    path('search_risks', views.search_risks, name='search_risks'),
    path('risk_register/<int:id>/',views.risk_details,name='risk_details'),
    path('/<int:id>/',views.delete_risk,name='delete_risk'),
    path('export_csv', views.export_csv, name='export-csv'),
    path('export_pdf', views.export_pdf, name='export_pdf'),



]