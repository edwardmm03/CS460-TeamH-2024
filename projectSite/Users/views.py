from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Users(request):
    template = loader.get_template('selectUser.html')
    return HttpResponse(template.render())

def Administrator(request):
    template = loader.get_template('Administrator.html')
    return HttpResponse(template.render())

def Instructor(request):
    template = loader.get_template('Instructor.html')
    context = {}
    return HttpResponse(template.render(context,request))

def Student(request):
    template = loader.get_template('Student.html')
    context = {}
    return HttpResponse(template.render(context, request))

def StudentResults(request):
    template = loader.get_template('StudentResults.html')
    return HttpResponse(template.render())

def CourseList(request):
    template = loader.get_template('CourseList.html')
    return HttpResponse(template.render())

def StudentList(request):
    template = loader.get_template('StudentList.html')
    return HttpResponse(template.render())
