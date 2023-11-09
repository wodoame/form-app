from django.shortcuts import render
from .models import VirtualForm
from django.http import JsonResponse, HttpResponse
import json

def index(request):
    
    fields = [
        {
            'field_name': 'Name', 
            'tag_name':'input', 
            'attributes':{
                'class':'form-control m-2',
                'type': 'text', 
                'name':'name'
            }
         },
        {
            'field_name': 'Age', 
            'tag_name':'input', 
            'attributes':{
                'class':'form-control is-valid m-2',
                'type': 'number', 
                'name':'age'
            }
         },
        {
            'field_name': 'Comment', 
            'tag_name':'textarea', 
            'attributes':{
                'class':'form-control m-2',
                'cols':'30', 
                'rows': '10', 
                'name': 'comment'
            }
         },
        {
            'field_name': 'country', 
            'tag_name':'input', 
            'attributes':{
                'class':'form-control m-2',
                'type':'text', 
            }
         },
    ]
    
    # data = json.dumps(fields)
    # print(data)
    
    # form = VirtualForm.objects.create(title='test form 1', form_fields=fields)
    return JsonResponse(data=fields, safe=False, status=200)
    

def home(request): 
    if request.method == 'POST': 
        print(request.POST) 
    return render(request, 'index.html', {})


def createForm(request): 
    return render(request, 'create-form.html', {})