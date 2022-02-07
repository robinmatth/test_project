from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Risks
from django.forms.widgets import NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#create an Add Risks form

class DateInput(forms.DateInput):
    input_type = 'date'

class AddRisksForm(ModelForm):
    class Meta:
        model = Risks
        fields = ('id','risk_description','risk_impact','risk_mitigation','risk_owner','risk_assignee','risk_status','risk_due_date')
        labels = {
            'risk_description':'',
            'risk_impact':'',
            'risk_mitigation':'',
            'risk_owner':'',
            'risk_assignee':'',
            'risk_status':'',
            'risk_due_date':'Please choose a due date for the risk: ',
        }
        IMPACT_CHOICES = [
            ('resources','Resources'),
            ('cost', 'Cost'),
            ('schedule','Schedule'),
            ('scope','Scope'),
            ('other','Other'),
        ]
        
        widgets = {
            'risk_description':forms.Textarea(attrs={'rows':6,'class': 'form-control', 'placeholder':'Risk Description'}),
            'risk_impact': forms.Select(attrs={'class':'form-select', 'placeholder':'other','style': 'width:200px'}),
            'risk_mitigation':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Mitigation'}),
            'risk_owner':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Owner'}),
            'risk_assignee':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Assignee'}),
            'risk_status':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Status'}),
            'risk_due_date': forms.DateInput(attrs={'class': 'form-control','type': 'date','style': 'width:200px'}),

        }



class UpdateRisksForm(ModelForm):
    class Meta:
        model = Risks
        fields = ('id','risk_description','risk_impact','risk_mitigation','risk_owner','risk_assignee','risk_status','risk_due_date')
        labels = {
            'risk_description':'',
            'risk_impact':'',
            'risk_mitigation':'',
            'risk_owner':'',
            'risk_assignee':'',
            'risk_status':'',
            'risk_due_date':'Please choose a due date for the risk: ',
        }
        IMPACT_CHOICES = [
            ('resources','Resources'),
            ('cost', 'Cost'),
            ('schedule','Schedule'),
            ('scope','Scope'),
            ('other','Other'),
        ]
        
        widgets = {
            'risk_description':forms.Textarea(attrs={'rows':6,'class': 'form-control', 'placeholder':'Risk Description'}),
            'risk_impact': forms.Select(attrs={'class':'form-select', 'placeholder':'other','style': 'width:200px'}),
            'risk_mitigation':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Mitigation'}),
            'risk_owner':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Owner'}),
            'risk_assignee':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Assignee'}),
            'risk_status':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Status'}),
            'risk_due_date': forms.DateInput(attrs={'class': 'form-control','type': 'date','style': 'width:200px'}),

        }


