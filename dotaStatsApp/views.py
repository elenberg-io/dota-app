from django.http import HttpResponse, Http404
from django.shortcuts import render
import os
from .models import Heroes
from myapp import settings


def index(request):
    return HttpResponse('Hello, this is index')


def home(request):
    # return HttpResponse('Hello, you are home')
    heroes = Heroes.objects.all()
    # images = os.listdir(os.path.join(settings.STATIC_URL, 'heroes/sb/'))
    return render(request, 'home.html', {
        'heroes': heroes,
        # 'images': images
    })


def hero_detailed(request, hero_id):
    # return HttpResponse(f'Hello, you are home {hero_id}')
    try:
        hero = Heroes.objects.get(hero_id=hero_id)
    except Heroes.DoesNotExist:
        raise Http404('hero not found')
    return render(request, 'hero_detailed.html', {
        'hero': hero,
    })
