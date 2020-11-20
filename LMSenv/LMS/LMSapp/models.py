from django.db import models

# username contact@rbmi
# pwd contact@rbmi

# Create your models here.
class Student_Registration(models.Model):
    Student_Registration_Number = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    Phone1 = models.CharField(max_length=15)
    Phone2 = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    Current_Address = models.CharField(max_length=200)
    Permanent_Address = models.CharField(max_length=200)
    Course = models.CharField(max_length=20)
    Year = models.CharField(max_length=10)
    Branch = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.fname+" "+self.Course+" Registration Number : "+str(self.Student_Registration_Number)
    
class Faculty_Registration(models.Model):
    Faculty_Registration_Number = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    Phone1 = models.CharField(max_length=15)
    Phone2 = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    Current_Address = models.CharField(max_length=200)
    Permanent_Address = models.CharField(max_length=200)
    Branch = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.fname+" "+self.Branch+" Registration Number: "+str(self.Faculty_Registration_Number)
    
class Book_Registration(models.Model):
    BookID = models.CharField(primary_key=True, max_length=20)
    BookName = models.CharField(max_length=50)
    Author1 = models.CharField(max_length=100)
    Author2 = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Page = models.CharField(max_length=10)
    Price = models.CharField(max_length=10)
    BookBelongsCourse = models.CharField(max_length=50)
    
    def __str__(self):
        return "Book Name: "+self.BookName+" Book Id: "+self.BookID+" Book Belongs: "+self.BookBelongsCourse
    
class Book_Issue_Student(models.Model):
    # ==========student info===================
    Student_Registration_Number = models.CharField(max_length=10)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    Phone1 = models.CharField(max_length=15)
    Phone2 = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    Current_Address = models.CharField(max_length=200)
    Permanent_Address = models.CharField(max_length=200)
    Course = models.CharField(max_length=20)
    Year = models.CharField(max_length=10)
    Branch = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    # =========book info=============
    BookID = models.CharField(max_length=20)
    BookName = models.CharField(max_length=50)
    Author1 = models.CharField(max_length=100)
    Author2 = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Page = models.CharField(max_length=10)
    Price = models.CharField(max_length=10)
    BookBelongsCourse = models.CharField(max_length=50)
    # =================book issue date infor===============
    Book_Issue_To_Student_Date = models.CharField(max_length=30)
    
    def __str__(self):
        return self.fname+" "+self.BookName+" "+self.Book_Issue_To_Student_Date