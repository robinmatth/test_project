from django.urls import path
from django.urls import include, path

from . import views
from .views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('risk_register', views.risk_register, name='risk_register'),
    path('risk_gallery/', views.risk_gallery, name="risk_gallery"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('risk_temp/', views.risk_temp, name="risk_temp"),
    path('add_risks', views.add_risks, name='add_risks'),
    
    path('update_risks', views.update_risks, name="update_risks"),
    path('update_risks/<int:id>', views.update_risks, name="update_risks"),
    
    path('search_risks', views.search_risks, name='search_risks'),
    path('risk_register/<int:id>/',views.risk_details,name='risk_details'),
    path('/<int:id>/',views.delete_risk,name='delete_risk'),
    path('export_csv', views.export_csv, name='export-csv'),
    path('export_pdf', views.export_pdf, name='export_pdf'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)