from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def register(request):
    ECFO = CredForm()
    d = {'ECFO':ECFO}
    if request.method == 'POST' and request.FILES:
        CFDO = CredForm(request.POST, request.FILES)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('Done')
        return HttpResponse('invalid Data')
    return render(request, 'register.html', d)