import random

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.db import models as orig_g

from .models import Mineral

def index(request):
    return HttpResponse("Welcome to the Minerals index.")
    # return render(request,
    #              'minerals/mineral_list.html',
    #              {'minerals': minerals})


def mineral_list(request):
    minerals = Mineral.objects.all()
    # output = ''
    # for mineral in minerals:
    #    output += str(mineral)
    #    output += ', '
    # return HttpResponse(output)
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_detail(request, pk):
    # mineral = Mineral.objects.get(pk=pk)
    mineral = get_object_or_404(Mineral, pk=pk)
    # attrlist = [attri for attri in dir(mineral)
    #            if not attri.startswith('__')]
    attrlist = list(filter(lambda a: not a.startswith('__'), dir(mineral)))
    mlist = [dflt for dflt in dir(orig_g.Model)]
    attrlist = list(filter(lambda x: x not in mlist, attrlist))
    no_list = ['DoesNotExist', 'MultipleObjectsReturned', '_state', 'id', 'name', 'imgcap', 'imgfile', 'objects']
    attrlist = list(filter(lambda x: x not in no_list, attrlist))
    for thing in attrlist:
        if thing.startswith('_'):
            attrlist.remove(thing)
    vallist = [getattr(mineral, thing) for thing in attrlist]
    result = zip(attrlist, vallist)
    attrlist = list(result)
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'attrlist': attrlist})

def random_mineral(request):
    pickfrom = len(Mineral.objects.all())
    prikey = random.randint(1, pickfrom)
    return mineral_detail(request, prikey)