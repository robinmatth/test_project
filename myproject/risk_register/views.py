from dataclasses import field
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
import django_tables2 as tables
from .models import Risks
from django.template import loader
from .forms import AddRisksForm
import csv, io, datetime,http
from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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
           return HttpResponseRedirect('/add_risks?submitted=True')
    else:
        form = AddRisksForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request,'add_risks.html', {'form': form, 'submited': submitted})

#Creating an export to PDF option (uses ReportLab library)

def export_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    risks = Risks.objects.all()
    
    lines = [
        'Print this text to prove this is working'
    ]
    # for risk in risks:
    #     lines.append(risks.risk_description)
    #     lines.append(risks.risk_mitigation)
    #     lines.append(risks.risk_owner)
    #     lines.append(risks.risk_assignee)
    #     lines.append(risks.risk_due_date)
    #     lines.append(risks.risk_status)
    # else:
    #     print('loop is not working')

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Risks.pdf')

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