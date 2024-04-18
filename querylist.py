#https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html

#python -m pip install mysql-connector-python
import mysql.connector

#to connect to mysql db on your own computer, use localhost
#to connect to a remote computer, use its IP address for host:
mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  passwd='root', #"mypassword",
  auth_plugin='mysql_native_password',
  database="university",
)
mycursor = mydb.cursor()
#print(mydb)


#THESE COMMANDS ARE FOR ADDING PAPERS AND FUNDING TO THE DATABASE:
#ALTER TABLE instructor ADD funding int;
#SET SQL_SAFE_UPDATES = 0;
#UPDATE instructor SET funding = 10000 * RAND() WHERE 1;
#CREATE TABLE papers( title varchar(100), publishdate DATE, instructor_id varchar(5), PRIMARY KEY (title, author), FOREIGN KEY (instructor_id) REFERENCES instructor(id));



class Admin:
   def __init__(self,id): 
      self.id = id
   def roster(sort): #Good
      order = True
      if sort != "name" or "dept" or "salary": 
         order = False
      if order:
         command = "SELECT * FROM instructor ORDER BY" + sort + ";"
      else:
         command = "SELECT * FROM instructor;"
      return command, "F1"
   def salary(): #Good
      command = "SELECT dept_name, min(salary), max(salary), round(avg(salary),0), FROM instructor GROUP BY dept_name;"
      return command, "F2"
   def performance(name,year,semester): #This took way too much time
      command = """
      SELECT T1.ccid, T2.csid, T3.funds, T4.cpapers FROM 
      (SELECT COUNT(course_id) AS ccid FROM teaches WHERE year="""+year+""" AND semester="""+semester+""" AND teacher_id="""+id+""") AS T1, 
      (SELECT COUNT(student_id) AS csid FROM takes WHERE year="""+year+""" AND semester="""+semester+""" 
      AND course_id IN (SELECT course_id FROM teaches WHERE teacher_id="""+id+"""))AS T2,
      (SELECT SUM(funding) AS funds FROM instructor WHERE id="""+id+""") AS T3,
      (SELECT COUNT(title) AS cpapers FROM papers WHERE instructor_id="""+id+""") AS T4;
      """ 
      return command, "F3"
class Professor:
   def __init__(self,id): 
      self.id = id
   def teaching(semester):#Good but mysql might give an error with group me, if so run: SET sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''));
      command = "SELECT teaches.course_id,teaches.sec_id,count(student_id) FROM teaches INNER JOIN takes ON takes.course_id = teaches.course_id WHERE takes.semester="+semester+" AND teacher_id="+id+";"
      return command, "F4"
   def students(course, section, semester): #Good, weird 2nd select to check if course is taught by the professor might be easier to implement something in frontend to show prof what their courses are.
      command = "SELECT student_id FROM takes WHERE course_id="+course+" semester="+semester+" AND section="+section+" AND course_id IN(SELECT course_id FROM teaches WHERE teacher_id="+id+" );"
      return command, "F5"
class Student:
  def __init__(self,id): 
      self.id = id
  def findcourse(dept,year,semester): #Good
     command = "SELECT course_id, sec_id FROM(SELECT course_id, sec_id FROM teaches WHERE year="+year+" AND semester="+semester+" UNION SELECT course_id, null from course WHERE dept_name"+dept+") AS T WHERE sec_id IS NOT NULL;"
     return command, "F6"
def run(command,format):
   mycursor.execute(command)
   myresult = mycursor.fetchall()
   if myresult == None:
      "No results found"
   else:
       match format:
          case "F1":
             for professor in myresult:
              print(professor)
          case "F2":
             for (dept, min, max, avg) in myresult:
              print(dept, min, max, avg)
          case "F3":
             for (ccount, scount, dtotal, ptotal) in myresult:
              print(ccount, scount, dtotal, ptotal)
          case "F4":
             for (section, scount) in myresult:
              print(section, scount)
          case "F5":
             for student in myresult:
              print(student)
          case "F6": 
             for (course,section) in myresult:
              print(course,section)
       

mycursor.close()
mydb.close()
