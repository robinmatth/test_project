from dataclasses import field
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
import django_tables2 as tables
from .models import Risks
from django.template import loader
from .forms import AddRisksForm
import csv, io, datetime,http,os
from django.http import FileResponse
from django.views.generic import View
import xhtml2pdf
from django.contrib import messages
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from risk_register.serializers import UserSerializer, GroupSerializer


def index(request):
    # return response
    return render(request, 'base.html')

def risk_register(request):
    items_list = Risks.objects.all()
    template = loader.get_template('risk_register.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))

def risk_gallery(request):
    items_list = Risks.objects.all()
    template = loader.get_template('risk_gallery.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))


def delete_risk(request, id):
    items_list = Risks.objects.get(pk=id)
    items_list.delete()
    return redirect('risk_register')

def search_risks(request):
    if request.method == "POST":
        searched = request.POST['searched']
        risks = Risks.objects.filter(risk_description__contains=searched)
        return render (request,"search_risks.html",
        {'searched':searched, 'risks':risks})
    else:

        return render (request,"search_risks.html",{})
 
def risk_details(request,id):
    items_list = Risks.objects.get(pk=id)
    context = {
        'items_list': items_list
    }
    return render (request,"risk_details.html",context)

def add_risks(request):
    submitted = False
    if request.method == "POST":
       form = AddRisksForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, ('You have succesfully added a risk to the register!'))
           return HttpResponseRedirect('/add_risks?submitted=True')
    else:
        form = AddRisksForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request,'add_risks.html', {'form': form, 'submited': submitted})

#Creating an export to PDF option (uses ReportLab library)

def export_pdf(request):
    pass

#This function exports CSV the risk register model into a CSV file
def export_csv(request):
    response=HttpResponse(content_type='text/csv')
    writer=csv.writer(response)
    writer = csv.writer(response)
    headers = ['id','Risk Description','Risk Mitigation','Risk Owner','Risk Assignee','Risk Due Date','Risk Status']
    writer.writerow(headers)    
    for risk in Risks.objects.all().values_list('id','risk_description','risk_mitigation','risk_owner','risk_assignee','risk_due_date','risk_status'):
        writer.writerow(risk)
    response['Content-Disposition']='attachement; filename=Risk-Register'+ str(datetime.datetime.now())+'.csv'
    return response

#required for PDF Generation
def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
                if not isinstance(result, (list, tuple)):
                        result = [result]
                result = list(os.path.realpath(path) for path in result)
                path=result[0]
        else:
                sUrl = settings.STATIC_URL        # Typically /static/
                sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                mUrl = settings.MEDIA_URL         # Typically /media/
                mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                if uri.startswith(mUrl):
                        path = os.path.join(mRoot, uri.replace(mUrl, ""))
                elif uri.startswith(sUrl):
                        path = os.path.join(sRoot, uri.replace(sUrl, ""))
                else:
                        return uri

        # make sure that file exists
        if not os.path.isfile(path):
                raise Exception(
                        'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]