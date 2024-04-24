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
        sql = """SELECT course_id, sec_id FROM teaches WHERE year = %s AND semester = %s AND course_id IN (SELECT course_id FROM course WHERE dept_name = %s)"""
        cursor.execute(sql, (year, semester, dept))
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
    name = request.POST.get('profName',0)
    year = request.POST.get('year',0)
    semester = request.POST.get('semester',0)
    
    cursor = connection.cursor()
    
    try:
        sql = """SELECT teaches.course_id,teaches.sec_id,count(student_id) AS studentCount FROM teaches INNER JOIN takes ON takes.course_id = teaches.course_id INNER JOIN instructor ON teaches.teacher_id = instructor.id WHERE takes.semester = %s AND takes.year = %s AND instructor.name = %s GROUP BY teaches.course_id, teaches.sec_id;"""
        cursor.execute(sql, (semester, year, name))
        data = dictfetchall(cursor)
        
    finally:
        cursor.close()
        
    print(data)
    template = loader.get_template('CourseList.html')
    context = {
        'rows' : data
    }
    
    return HttpResponse(template.render(context,request))

def StudentList(request):
    name = request.POST.get('profName',0)
    year = request.POST.get('year',0)
    semester = request.POST.get('semester',0)

    template = loader.get_template('StudentList.html')
    return HttpResponse(template.render())

def InstructorList(request):
    sort = request.POST.get('sort',0)

    cursor = connection.cursor()
    
    try:
        sql = """SELECT * FROM instructor ORDER BY %s """ %sort
        cursor.execute(sql)
        data = dictfetchall(cursor)
    finally:
        cursor.close()

    print(data)
    template = loader.get_template('InstructorList.html')
    context = {
        'rows' : data
    }

    return HttpResponse(template.render(context,request))



def DeptSals(request):

    cursor = connection.cursor()
    
    try:
        sql = """SELECT dept_name, min(salary), max(salary), round(avg(salary),0) FROM instructor GROUP BY dept_name;"""
        cursor.execute(sql)
        data = dictfetchall(cursor)
    finally:
        cursor.close()

    print(data)
    template = loader.get_template('DeptSals.html')
    context = {
        'rows' : data
    }
    return HttpResponse(template.render(context,request))

def Performance(request):
    name = request.POST.get('profName',0)
    year = request.POST.get('year',0)
    semester = request.POST.get('semester',0)

    template = loader.get_template('Performance.html')
    return HttpResponse(template.render())
