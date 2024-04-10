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

class Admin:
   #All mysql commands are best guess without looking at the database because its not setup on this computer
   def __init__(self,id): 
      self.id = id
   def roster(sort):
      order = True
      if sort != "name" or "dept" or "salary": #this line feels wrong, might cause errors might not we will find out
         order = False
      if order:
         command = "SELECT * FROM professor ORDER BY" + sort + ";"
      else:
         command = "SELECT * FROM professor;"
      return command, "F1"
   def salary():
      command = ""#Need to figure out mysql command
      return command, "F2"
   def preformance(name,year,semester):
      #Needs some sort of error checking? Might just be bundled in run function
      command = "SELECT COUNT(section), COUNT(student), SUM(?), SUM(?) FROM professor WHERE name = " + name + ", year = " + year + ", semester = " + semester + ";" #WRONG STUPID IDIOT also add papers to database?
      return command, "F3"
class Professor:
   def __init__(self,id): 
      self.id = id
   def teaching(semester):
      command = "SELECT course, section, count(student) where semester = " + semester + "ORDER BY section;"
      return command, "F4"
   def students(section, semester): #Does it need a filter to check if the professor taught it(mentioned in specification but not in a solid yes or no way)
      command = "SELECT student WHERE semester = " + semester + " AND section = " + section + ";"
      return command, "F5"
class Student:
  def __init__(self,id): 
      self.id = id
  def findcourse(dept,year,semester):
     command = "SELECT course WHERE dept = " + dept + " AND year = " + year + " AND semester = " + semester + ";"
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
             for (min, max, avg) in myresult:
              print(min, max, avg)
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
             for section in myresult:
              print(section)
       

mycursor.close()
mydb.close()
