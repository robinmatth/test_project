from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Risks

#create an Add Risks form

class AddRisksForm(ModelForm):
    class Meta:
        model = Risks
        fields = ('id','risk_description','risk_mitigation','risk_owner','risk_assignee','risk_status')
        labels = {
            'risk_description':'',
            'risk_mitigation':'',
            'risk_owner':'',
            'risk_assignee':'',
            'risk_status':'',
        }
        widgets = {
            'risk_description':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Description'}),
            'risk_mitigation':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Mitigation'}),
            'risk_owner':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Owner'}),
            'risk_assignee':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Assignee'}),
            'risk_status':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Risk Status'}),
        }