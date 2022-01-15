from dataclasses import field
import http
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
import django_tables2 as tables
from .models import Risks
from django.template import loader

import csv
import datetime


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

#This function exports the risk register model into a CSV file
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

def delete_risk(request, id):
    risk = Risks.objects.get(pk=id)
    risk.delete()
    return redirect('')
 
def risk_details(request,id):
    risk = Risks.objects.get(pk=id)
    context = {
        'risk': risk
    }
    return render (request,"risk_details.html",context)