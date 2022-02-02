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
            'risk_impact':' Select a Risk Category',
            'risk_mitigation':'',
            'risk_owner':'',
            'risk_assignee':'',
            'risk_status':'',
            'risk_due_date':'Choose a Risk due date',
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
            # 'risk_due_date': (DateInput),
            'risk_due_date': DateInput(),
        }
        choices =forms.ChoiceField(label="other", choices=IMPACT_CHOICES, required=True),


class UpdateRisksForm(ModelForm):
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
            'risk_due_date':'Choose a Risk due date',
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
            # 'risk_due_date': (DateInput),
            'risk_due_date': DateInput(),
        }
        choices =forms.ChoiceField(label="other", choices=IMPACT_CHOICES, required=True),

