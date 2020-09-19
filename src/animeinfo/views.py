from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import AnimeSeries

# Create your views here.


def index(request):
    all_series = AnimeSeries.objects.all()
    context = {
        'anime': all_series
    }
    return render(request, 'animeinfo/index.html', context)


def info(request, slug):
    anime = get_object_or_404(AnimeSeries, slug=slug)
    context = {
        'anime': anime
    }
    return render(request, 'animeinfo/info.html', context)    
