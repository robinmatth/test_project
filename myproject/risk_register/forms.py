from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Risks

#create an Add Risks form

class AddRisksForm(ModelForm):
    class Meta:
        model = Risks
        fields = ('id','risk_description','risk_impact','risk_mitigation','risk_owner','risk_assignee','risk_status')
        labels = {
            'risk_description':'',
            'risk_impact':' Select a Risk Category',
            'risk_mitigation':'',
            'risk_owner':'',
            'risk_assignee':'',
            'risk_status':'',
        }
        IMPACT_CHOICES = [
            ('resources','RESOURCES'),
            ('cost', 'COST'),
            ('schedule','SCHEDULE'),
            ('scope','SCOPE'),
            ('other','OTHER'),
        ]
        
        widgets = {
            'risk_description':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Description'}),
            
            'risk_mitigation':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Mitigation'}),
            'risk_owner':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Owner'}),
            'risk_assignee':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Assignee'}),
            'risk_status':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Status'}),
        }
        choices =forms.ChoiceField(label="other", choices=IMPACT_CHOICES, required=True),