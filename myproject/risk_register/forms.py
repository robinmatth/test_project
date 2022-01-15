from socket import fromshare
from django import forms 
from django.forms import ModelForm
from .models import Risks

#create an Add Risks form

class AddRisksForm(ModelForm):
    class Meta:
        model = Risks
        fields = ('id','risk_description','risk_mitigation','risk_owner','risk_assignee','risk_status')