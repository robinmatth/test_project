# tutorial/tables.py
import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "people.html"
        fields = ("name", )