from django.db import models

class Course(models.Model):
    course_id = models.CharField(primary_key = True, max_length =8)
    title = models.CharField(max_length=64, blank = True, null = True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column = 'dept_name', blank = True, null= True)
    credits = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'Course'

class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length = 32)
    building = models.CharField(max_length=32, blank = True, null = True)
    budget = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'Department'

class Instructor(models.Model):
    id = models.CharField(primary_key = True, max_length=5)
    name = models.CharField(max_length=32, blank = True, null = True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column = 'dept_name', blank = True, null= True)
    salary = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'Instructor'

class Student(models.Model):
    student_id = models.CharField(primary_key = True, max_length = 8)
    name = models.CharField(max_length = 32, blank = True, null = True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column = 'dept_name', blank = True, null= True)
    total_credits = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'Student'

class Section(models.Model):
    course_id = models.OneToOneField(Course, models.DO_NOTHING, primary_key = True)
    sec_id = models.CharField(max_length =3)
    semester = models.IntegerField()
    year = models.IntegerField()
    buidling = models.CharField(max_length = 32, blank = True, null = True)
    room = models.CharField(max_length = 8, blank = True, null = True)
    capacity = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'Section'
        unique_together = (('course_id','sec_id','semester','year'),)

class Prereq(models.Model):
    course_id = models.OneToOneField(Course, models.DO_NOTHING,primary_key = True)
    preq_id = models.ForeignKey(Course, models.DO_NOTHING, related_name='prereq_preq_set')

    class Meta:
        managed = False
        db_table = 'Prereq'
        unique_together=(('course_id', 'preq_id'),)

class Teaches(models.Model):
    course_id = models.OneToOneField(Course, models.DO_NOTHING,primary_key = True)
    sec_id = models.CharField(max_length=4)
    semester = models.IntegerField()
    year = models.IntegerField()
    teacher_id = models.ForeignKey('Instructor', models.DO_NOTHING, db_column = 'id')

    class Meta:
        managed = False
        db_table = 'Teaches'
        unique_together =(('course_id','sec_id','semester','year','teacher_id'),)

class Takes(models.Model):
    student_id = models.ForeignKey('Student', models.DO_NOTHING, db_column = 'student_id')
    course_id = models.OneToOneField(Course, models.DO_NOTHING,primary_key = True)
    sec_id = models.CharField(max_length =4)
    semester = models.IntegerField()
    year = models.IntegerField()
    grade = models.CharField(max_length = 2, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'Takes'
        unique_together = (('student_id','course_id','sec_id','semester','year'),)
