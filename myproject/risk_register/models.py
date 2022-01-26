from django.db import models
import django_tables2 as tables
IMPACT_CHOICES = (
    ('please select','Please select'),
    ('resources','Resources'),
    ('cost', 'Cost'),
    ('schedule','Schedule'),
    ('scope','Scope'),
    ('other','Other'),
)


class Risks(models.Model):
    class Meta:
        verbose_name = 'Project Risks'
        verbose_name_plural = 'Project Risks'

    risk_description = models.CharField(max_length=200)
    risk_owner = models.CharField(max_length=100)
    risk_impact = models.CharField(max_length=15, choices=IMPACT_CHOICES, default='please select')
    risk_date = models.DateField(blank=True, null=True)
    risk_mitigation = models.CharField(max_length=500)
    risk_due_date = models.DateField(blank=True, null=True)
    risk_status = models.CharField(max_length=200)
    risk_assignee = models.CharField(max_length=200)
    risk_rank = models.IntegerField(default=0)
