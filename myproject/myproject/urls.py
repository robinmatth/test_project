"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from risk_register import urls, views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'risks', views.RisksViewSet)
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views
from django.contrib.auth import views as authentication_views



urlpatterns = [
    path('', views.index, name="index"),
    path('risk_register/', views.risk_register, name="risk_register"),
    path('risk_gallery/', views.risk_gallery, name="risk_gallery"),

    path('add_risks/', views.add_risks, name="add_risks"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('search_risks/', views.search_risks, name="search_risks"),
    path('risk_register/<int:id>/', views.risk_details, name="risk_details"),
    path('delete_risk/<int:id>/', views.delete_risk, name="delete_risk"),
    path('export_csv', views.export_csv, name='export-csv'),
    path('export_pdf', views.export_pdf, name='export_pdf'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('risk_temp/', views.risk_temp, name="risk_temp"),
    # Authentication Paths and User Profile
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),  
    path('profile/', user_views.profilepage, name="profile"), 
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
