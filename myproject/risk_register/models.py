from django.db import models
import django_tables2 as tables
IMPACT_CHOICES = (
    ('resources','RESOURCES'),
    ('cost', 'COST'),
    ('schedule','SCHEDULE'),
    ('scope','SCOPE'),
    ('other','OTHER'),
)


class Risks(models.Model):
    risk_description = models.CharField(max_length=200)
    risk_owner = models.CharField(max_length=100)
    risk_impact = models.CharField(max_length=15, choices=IMPACT_CHOICES, default='other')
    risk_date = models.DateTimeField(blank=True, null=True,auto_now_add=False)
    risk_mitigation = models.CharField(max_length=500)
    risk_due_date = models.DateTimeField(blank=True, null=True,auto_now_add=False)
    risk_status = models.CharField(max_length=200)
    risk_assignee = models.CharField(max_length=200)
    risk_rank = models.IntegerField(default=0)
