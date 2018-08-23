from django.shortcuts import render
from django.http import HttpResponse

from .models import Mineral

def index(request):
    return HttpResponse("Welcome to the Minerals index.")

def mineral_list(request):
    minerals = Mineral.objects.all()
    output = ''
    for mineral in minerals:
        output += str(mineral)
        output += ', '
    # output = ', '.join(minerals)
    return HttpResponse(output)