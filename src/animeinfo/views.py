from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import AnimeSeries

# Create your views here.


def index(request):
    all_series = AnimeSeries.objects.all()
    context = {
        'anime': all_series
    }
    template = loader.get_template('animeinfo/index.html')
    return HttpResponse(template.render(context, request))
