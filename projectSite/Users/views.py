from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Users(request):
    template = loader.get_template('selectUser.html')
    return HttpResponse(template.render())

def Administrator(request):
    template = loader.get_template('Administrator.html')
    context = {}
    return HttpResponse(template.render(context,request))

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

def InstructorList(request):
    template = loader.get_template('InstructorList.html')
    return HttpResponse(template.render())

def DeptSals(request):
    template = loader.get_template('DeptSals.html')
    return HttpResponse(template.render())

def Performance(request):
    template = loader.get_template('Performance.html')
    return HttpResponse(template.render())
