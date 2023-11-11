from django.shortcuts import render, redirect
from .models import VirtualForm
from django.http import JsonResponse, HttpResponse
import json

def index(request):
    if request.method == 'POST': 
        formData = json.loads(request.body) # To convert to a json string for storage in the database
        form_title = formData.get('form_title')
        form_fields = json.dumps(formData.get('fields'))
        VirtualForm.objects.create(title=form_title, form_fields=form_fields)
    formData = json.loads(VirtualForm.objects.last().form_fields)
    return JsonResponse(data=formData, safe=False)

def home(request): 
    if request.method == 'POST': 
        print(request.POST) 
    return render(request, 'index.html', {})


def createForm(request): 
    return render(request, 'create-form.html', {})

def previewForms(request):
    forms = VirtualForm.objects.all()
    return render(request, 'preview-forms.html', {'forms':forms})

def showForm(request, id):
    form = VirtualForm.objects.get(id=id)
    context = {'form': form}
    return render(request, 'index.html', context)
    