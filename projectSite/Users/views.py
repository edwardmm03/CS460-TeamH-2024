from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Users(request):
    template = loader.get_template('selectUser.html')
    return HttpResponse(template.render())

def Student(request):
    template = loader.get_template('Student.html')
    return HttpResponse(template.render())