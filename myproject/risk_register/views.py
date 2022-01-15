from dataclasses import field
import http
from django.http import HttpResponse
import django_tables2 as tables
from .models import Risks
from django.template import loader
from django.views.generic import ListView
from .models import Person
from .tables import Person
import csv
import datetime

class PersonListView(ListView):
    model = Person
    template_name = 'people.html'

def base(request):
    items_list = Risks.objects.all()
    template = loader.get_template('base.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    items_list = Risks.objects.all()
    template = loader.get_template('home.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))

def export_csv(request):

    response=HttpResponse(content_type='text/csv')
   
    writer=csv.writer(response)
    # the csv writer
    writer = csv.writer(response)
    headers = ['Risk Description','Risk Mitigation','Risk Owner','Risk Assignee','Risk Due Date','Risk Status']
    writer.writerow(headers)
    
    for risk in Risks.objects.all().values_list('risk_description','risk_mitigation','risk_owner','risk_assignee','risk_due_date','risk_status'):
        writer.writerow(risk)
    
    response['Content-Disposition']='attachement; filename=Risk-Register'+ str(datetime.datetime.now())+'.csv'
    return response


    # headers = ['Risk Description','Risk Mitigation','Risk Owner','Risk Assignee','Risk Due Date','Risk Status']
    # writer.writerow(headers)
    # queryset = Risks.objects.all()

    # for risk in queryset:
    #     row = [risk.risk_description,risk.risk_mitigation,risk.risk_owner,risk.risk_assignee,risk.risk_due_date,risk.risk_status]
    #     writer.writerows(row)
    #     # writer.writerow([risk.risk_description,risk.risk_mitigation,risk.risk_owner,risk.risk_assignee,risk.risk_due_date,risk.risk_status])
    # return response
 