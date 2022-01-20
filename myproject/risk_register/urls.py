from django.urls import path
from django.urls import include, path

from . import views
from .views import index



urlpatterns = [
    path('risk_register', views.risk_register, name='risk_register'),
    path('risk_gallery/', views.risk_gallery, name="risk_gallery"),
    path('add_risks', views.add_risks, name='add_risks'),
    path('search_risks', views.search_risks, name='search_risks'),
    path('risk_register/<int:id>/',views.risk_details,name='risk_details'),
    path('/<int:id>/',views.delete_risk,name='delete_risk'),
    path('export_csv', views.export_csv, name='export-csv'),
    path('export_pdf', views.export_pdf, name='export_pdf'),
    # path('', include(router.urls)),
   # path('api_auth', views.export_pdf, name='api_auth'),
   # path(r'^api_auth/', include(('my_project.urls', 'risk_register'), namespace='risk_register')),

]