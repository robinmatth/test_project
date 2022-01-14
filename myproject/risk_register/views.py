from django.http import HttpResponse
import django_tables2 as tables
from .models import Risks
from django.template import loader
from django.views.generic import ListView
from .models import Person
from .tables import Person


class PersonListView(ListView):
    model = Person
    template_name = 'people.html'



def base(request):
    items_list = Risks.objects.all()
    template = loader.get_template('base.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    items_list = Risks.objects.all()
    template = loader.get_template('home.html')
    context = {
        'items_list': items_list,
    }
    return HttpResponse(template.render(context, request))
