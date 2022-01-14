from django.db import models
import django_tables2 as tables

class Risks(models.Model):
    risk_description = models.CharField(max_length=200)
    risk_owner = models.CharField(max_length=100)
    risk_date = models.DateTimeField('Date Risk was discovered')
    risk_mitigation = models.CharField(max_length=500)
    risk_due_date = models.DateTimeField('Date the risk is expected to be resolved')
    risk_status = models.CharField(max_length=200)
    risk_assignee = models.CharField(max_length=200)
    risk_rank = models.IntegerField(default=0)

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
