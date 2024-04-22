from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import mysql.connector
from django.db import connection
from .models import Course

#Converts query results to a list of dictionary objects
def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


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
    dept = request.POST.get('department',0)
    year = request.POST.get('year',0)
    semester = request.POST.get('semester',0)

    cursor = connection.cursor()

    try:
        cursor.execute(f'''SELECT course_id, sec_id FROM(SELECT course_id, sec_id FROM teaches WHERE {year} = year AND {semester} = semester UNION SELECT course_id, null from course WHERE \"{dept}\" = dept_name) AS T WHERE sec_id IS NOT NULL;''')
        data = dictfetchall(cursor)
    finally:
        cursor.close()

    print(data)
    template = loader.get_template('StudentResults.html')
    context = {
        'rows' : data
    }

    return HttpResponse(template.render(context,request))

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
