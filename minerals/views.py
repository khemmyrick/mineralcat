from django.shortcuts import render
from django.http import HttpResponse

from .models import Mineral

def index(request):
    return HttpResponse("Welcome to the Minerals index.")

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
