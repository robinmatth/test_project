from audioop import avg
from dataclasses import field
from importlib import resources
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
import django_tables2 as tables
from .models import Projects, Risks
from django.template import loader
from .forms import AddRisksForm, UpdateRisksForm
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
from risk_register.serializers import UserSerializer, GroupSerializer, RisksSerializer
from django.db.models import Count
from django.db.models import Avg
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

def index(request):
    # return response
    return render(request, 'base.html')

def risk_register(request):
    items_list = Risks.objects.all()
    project_list = Projects.objects.all()
    template = loader.get_template('risk_register.html')
    context = {
        'items_list': items_list,
        'project_list': project_list,
    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    labels = []
    data = []

    queryset = Risks.objects.order_by('-risk_impact')[:10]
    count = Risks.objects.count()

    cost_count = Risks.objects.filter(risk_impact='cost').count()
    schedule_count = Risks.objects.filter(risk_impact='schedule').count()   
    for item in queryset:
        labels.append(item.risk_impact)
        data.append(item.id)

    return render(request, 'dashboard.html', {
        'labels': labels,
        'data': data,
        'count': count,
        'cost_count': cost_count,
        'schedule_count': schedule_count,
    })


def risk_gallery(request):
    submitted = False
    if request.method == "POST":
       form = AddRisksForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,f'You have added a risk to the Register!')
           return HttpResponseRedirect('/risk_gallery')
    else:
        form = AddRisksForm
        if 'submitted' in request.GET:
            submitted = True

    items_list = Risks.objects.all()
    template = loader.get_template('risk_gallery.html')
    context = {
        'items_list': items_list,
        'form': form,
        'submitted': submitted,
    }
    return HttpResponse(template.render(context, request))


def delete_risk(request, id):
    items_list = Risks.objects.get(pk=id)
    items_list.delete()
    messages.success(request,f'You have deleted item # {id} from the Risk Register')
    return redirect('risk_gallery')

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
           messages.success(request,f'You have added a risk to the Register!')
           return HttpResponseRedirect('/add_risks?submitted=True')
    else:
        form = AddRisksForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request,'add_risks.html', {'form': form, 'submited': submitted})

def update_risks(request, id):
    risks = Risks.objects.get(id=id)
    form = UpdateRisksForm(instance=risks)
    if request.method == "POST":
       form = AddRisksForm(request.POST, instance=risks)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/risk_register')
           messages.success(request,f'You have updated the Risk in the Register!')
    context = {'form': form}
            
    return render(request,'update_risks.html', context)



def risk_temp(request):
    submitted = False
    if request.method == "POST":
       form = AddRisksForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,f'You have added a risk to the Register!')
           return HttpResponseRedirect('/risk_temp?submitted=True')
    else:
        form = AddRisksForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request,'risk_temp.html', {'form': form, 'submited': submitted})










def export_pdf(request):
    items_list = Risks.objects.all()
    template_path = 'risk_register.html'
    context = {'items_list': items_list,}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

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

class RisksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Risks.objects.all()
    serializer_class = RisksSerializer
    permission_classes = [permissions.IsAuthenticated]




 
