from django.shortcuts import render, redirect
from .models import VirtualForm
from django.http import JsonResponse, HttpResponse
import json

def index(request):
    if request.method == 'POST': 
        form_fields = json.dumps(json.loads(request.body)) # To convert to a json string for storage in the database
        VirtualForm.objects.create(title='Test Form', form_fields=form_fields)
    formData = json.loads(VirtualForm.objects.last().form_fields)
    return JsonResponse(data=formData, safe=False)

def home(request): 
    if request.method == 'POST': 
        print(request.POST) 
    return render(request, 'index.html', {})


def createForm(request): 
    return render(request, 'create-form.html', {})