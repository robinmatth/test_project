from django.db import models
from django.contrib.auth.models import User

IMPACT_CHOICES = (
    ('choose a category','Choose a category'),
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
    risks_id = models.IntegerField(default=0)
    risk_description = models.CharField(max_length=200)
    risk_owner = models.CharField(max_length=100)
    risk_impact = models.CharField(max_length=30, choices=IMPACT_CHOICES, default='choose a category')
    risk_date = models.DateField(blank=True, null=True)
    risk_mitigation = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    risk_due_date = models.DateField(blank=True, null=True, default='Pick a due date')
    risk_status = models.CharField(max_length=200)
    risk_assignee = models.CharField(max_length=200)
    

class Projects(models.Model):
    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'
    
    project_description = models.CharField(max_length=200)
    risks = models.ManyToManyField(Risks)
    


