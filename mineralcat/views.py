from django.shortcuts import render

def index(request):
    return render(request, 'home.html')
    # return HttpResponse('Howdy!')