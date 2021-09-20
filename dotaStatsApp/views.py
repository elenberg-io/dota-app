from django.http import HttpResponse, Http404
from django.shortcuts import render
import os
from .models import Heroes
from .forms import HeroForm
from myapp import settings


def index(request):
    return HttpResponse('Hello, this is index')


def home(request):
    heroes = Heroes.objects.all()
    # images = os.listdir(os.path.join(settings.STATIC_URL, 'heroes/sb/'))
    return render(request, 'home.html', {
        'heroes': heroes,
    })


def hero_detailed(request, dname):
    try:
        hero = Heroes.objects.get(dname=dname)
    except Heroes.DoesNotExist:
        raise Http404('hero not found')
    return render(request, 'hero_detailed.html', {
        'hero': hero,
    })


def hero_suggestion(request):
    heroes = Heroes.objects.all()
    form = HeroForm()
    print(request.method, request.POST.get('hero'))
    if request.method=="POST":
        base_str = Heroes.objects.values_list('base_str', flat=True).filter(localized_name=request.POST.get('hero'))
        base_agi = Heroes.objects.values_list('base_agi', flat=True).filter(
            localized_name=request.POST.get('hero'))
        base_int = Heroes.objects.values_list('base_int', flat=True).filter(
            localized_name=request.POST.get('hero'))

        print(base_str, base_agi, base_int)
        print(request.POST.getlist('params'))
    return render(request, 'hero_suggestion.html', {
        'heroes': heroes,
        'form1': form,
        'form2': form
    })



# def hero_suggestion_produce(request):
#     # context = {}
#     # form = HeroForm(request.POST or None)
#     # context['form'] = form
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create form instances and populate them with data from the request
#         form1 = HeroForm(request.POST, prefix="form1")
#         form2 = HeroForm(request.POST, prefix="form2")
#         print(request.POST)
#         print(form1)
#         print(form2)
#         print(list(request.POST.values()))
#         print(form1.is_valid())
#         print(form1.errors.as_json())
#         print(form2.is_valid())
#         print(form2.errors.as_json())
#         # print(form1.cleaned_data['dname'])
#
#         # temp = form.cleaned_data.get("dname")
#         # print(temp)
#     # Otherwise, if it's any other method we create a blank form
#     else:
#         form1 = HeroForm(prefix="form1")
#         form2 = HeroForm(prefix="form2")
#     return render(request, "hero_suggestion_produce.html", {"form1": form1,
#                                                             "form2": form2})
