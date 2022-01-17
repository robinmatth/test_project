from dataclasses import field
import http
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
import django_tables2 as tables
from .models import Risks
from django.template import loader
from .forms import AddRisksForm
import csv
import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

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

def export_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    headers = ['id','Risk Description','Risk Mitigation','Risk Owner','Risk Assignee','Risk Due Date','Risk Status']
        
    #p = Risks.objects.all().values_list('id','risk_description','risk_mitigation','risk_owner','risk_assignee','risk_due_date','risk_status'),

    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')