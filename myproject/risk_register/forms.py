from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Risks
from django.forms.widgets import NumberInput

#create an Add Risks form

class AddRisksForm(ModelForm):
    class Meta:
        model = Risks
        fields = ('id','risk_description','risk_impact','risk_mitigation','risk_owner','risk_assignee','risk_status','risk_due_date')
        labels = {
            'risk_description':'',
            'risk_impact':' Select a Risk Category',
            'risk_mitigation':'',
            'risk_owner':'',
            'risk_assignee':'',
            'risk_status':'',
            'risk_due_date':'',
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
            
            'risk_mitigation':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Mitigation'}),
            'risk_owner':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Owner'}),
            'risk_assignee':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Assignee'}),
            'risk_status':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Status'}),
            
        }
        choices =forms.ChoiceField(label="other", choices=IMPACT_CHOICES, required=True),
        risk_due = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M']),