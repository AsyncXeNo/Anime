from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def landing(request):
    template = loader.get_template('home/landing.html')
    return HttpResponse(template.render({}, request))
