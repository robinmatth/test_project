from django.urls import path

from . import views
from risk_register.views import PersonListView

urlpatterns = [
    # ex: /index path using base.html
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('people/', PersonListView.as_view())

    
]