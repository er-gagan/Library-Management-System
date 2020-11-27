from django.shortcuts import redirect, render
from django.http import HttpResponse
from LMSapp.models import Book_Issue_Student, Student_Registration,Faculty_Registration,Book_Registration
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# username contact@rbmi
# pwd contact@rbmi

def home(request):
    return render(request,"LMSapp/home.html")

def AdminLoginPage(request):
    return render(request,"LMSapp/AdminLoginPage.html")

def StudentLoginPage(request):
    return render(request,"LMSapp/StudentLoginPage.html")

@csrf_exempt
def AdminWelcomePage(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return render(request,"LMSapp/AdminWelcomePage.html")
        else:
            messages.error(request,"Invallid Credentials, Please Try Again")
            return render(request,"LMSapp/AdminLoginPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

@csrf_exempt
def LogOut(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect("/")

def StudentRegistrationPage(request):
    if request.method == 'POST':
        return render(request,"LMSapp/StudentRegistrationPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def BookIssueToStudent(request):
    if request.method == 'POST':
        return render(request,"LMSapp/BookIssueToStudent.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def BookSubmitByStudent(request):
    if request.method == 'POST':
        return render(request,"LMSapp/BookSubmitByStudent.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def FacultyRegistrationPage(request):
    if request.method == 'POST':
        return render(request,"LMSapp/FacultyRegistrationPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def BookIssueToFaculty(request):
    if request.method == 'POST':
        return render(request,"LMSapp/BookIssueToFaculty.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def BookSubmitByFaculty(request):
    if request.method == 'POST':
        return render(request,"LMSapp/BookSubmitByFaculty.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def BookRegistrationPage(request):
    if request.method == 'POST':
        return render(request,"LMSapp/BookRegistrationPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def ViewAllBookPage(request):
    if request.method == 'POST':
        return render(request,"LMSapp/ViewAllBookPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def ViewBooksByBranch(request):
    if request.method == 'POST':
        return render(request,"LMSapp/ViewBooksByBranch.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

def Student_Registration_Data(request):
    if request.method == 'POST':
        fname = request.POST['fname'].upper()
        mname = request.POST['mname'].upper()
        lname = request.POST['lname'].upper()
        Phone1 = request.POST['Phone1']
        Phone2 = request.POST['Phone2']
        email = request.POST['email']
        city = request.POST['city'].capitalize()
        district = request.POST['district'].capitalize()
        state = request.POST['state']
        pin = request.POST['pin']
        Current_Address = request.POST['CurrentAddress']
        Permanent_Address = request.POST['PermanentAddress']
        Course = request.POST['Course']
        Year = request.POST['Year']
        Branch = request.POST['Branch']
        Gender = request.POST['Gender']
        if Phone1 == Phone2:
            messages.error(request,"Please enter different phone number")
            return render(request,"LMSapp/StudentRegistrationPage.html")    
        elif Student_Registration.objects.filter(fname__iexact = fname):
            if Student_Registration.objects.filter(Phone1__iexact = Phone1):
                messages.error(request,"Record already exist")
                return render(request,"LMSapp/StudentRegistrationPage.html")
            else:
                Student_Registration(fname = fname,mname = mname,lname = lname,Phone1 = Phone1,Phone2 = Phone2,email = email,city = city,district = district,state = state,pin = pin,Current_Address = Current_Address,Permanent_Address = Permanent_Address,Course = Course,Year = Year,Branch = Branch,Gender = Gender).save()
                obj = Student_Registration.objects.filter(Phone1__iexact = Phone1)
                reg_Num = None
                for i in obj:
                    reg_Num = i.Student_Registration_Number
                msg = "Student registered successfully, Name: "+fname+", Registration Number: "+str(reg_Num)
                messages.success(request,msg)
                return render(request,"LMSapp/StudentRegistrationPage.html")
        else:
            Student_Registration(fname = fname,mname = mname,lname = lname,Phone1 = Phone1,Phone2 = Phone2,email = email,city = city,district = district,state = state,pin = pin,Current_Address = Current_Address,Permanent_Address = Permanent_Address,Course = Course,Year = Year,Branch = Branch,Gender = Gender).save()
            obj = Student_Registration.objects.filter(Phone1__iexact = Phone1)
            reg_Num = None
            for i in obj:
                reg_Num = i.Student_Registration_Number
            msg = "Student registered successfully, Name: "+fname+", Registration Number: "+str(reg_Num)
            messages.success(request,msg)
            return render(request,"LMSapp/StudentRegistrationPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def Book_Registration_Data(request):
    if request.method == 'POST':
        BookID = request.POST['BookID']
        BookName = request.POST['BookName']
        Author1 = request.POST['Author1']
        Author2 = request.POST['Author2']
        Publisher = request.POST['Publisher']
        Page = request.POST['Page']
        Price = request.POST['Price']
        BookBelongsCourse = request.POST['BookBelongsCourse']
        Book_Registration(BookID = BookID,BookName = BookName,Author1 = Author1,Author2 = Author2,Publisher = Publisher,Page = Page,Price = Price,BookBelongsCourse = BookBelongsCourse).save()
        return render(request,"LMSapp/BookRegistrationPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def Faculty_Registration_Data(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        Phone1 = request.POST['Phone1']
        Phone2 = request.POST['Phone2']
        email = request.POST['email']
        city = request.POST['city']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        Current_Address = request.POST['Current_Address']
        Permanent_Address = request.POST['Permanent_Address']
        Branch = request.POST['Branch']
        Gender = request.POST['Gender']

        if Phone1 == Phone2:
            messages.error(request,"Phone number must be unique")
        elif Faculty_Registration.objects.filter(Phone1__iexact=Phone1):
            messages.error(request,"Record already exist in database")
        else:
            Faculty_Registration(fname = fname,mname = mname,lname = lname,Phone1 = Phone1,Phone2 = Phone2,email = email,city = city,district = district,state = state,pin = pin,Current_Address = Current_Address,Permanent_Address = Permanent_Address,Branch = Branch,Gender = Gender).save()
            Reg = None
            for reg in Faculty_Registration.objects.filter(Phone1__iexact=Phone1):
                Reg = reg.Faculty_Registration_Number
            messages.success(request,"Record stored into database with Registration Number: "+Reg)
        return render(request,"LMSapp/FacultyRegistrationPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def BookIssueToStudent_Id_Check(request):
    if request.method == 'POST':
        Student_Library_Registration_Number = request.POST['BookIssueToStudent']
        if Student_Registration.objects.filter(Student_Registration_Number=Student_Library_Registration_Number):
            Student_data = Student_Registration.objects.get(Student_Registration_Number=Student_Library_Registration_Number)
            context={'RegNo':Student_data.Student_Registration_Number,'fname':Student_data.fname,'mname':Student_data.mname,'lname':Student_data.lname,'Phone1':Student_data.Phone1,'Phone2':Student_data.Phone2,'email':Student_data.email,'city':Student_data.city,'district':Student_data.district,'state':Student_data.state,'pin':Student_data.pin,'Current_Address':Student_data.Current_Address,'Permanent_Address':Student_data.Permanent_Address,'Course':Student_data.Course,'Year':Student_data.Year,'Branch':Student_data.Branch,'Gender':Student_data.Gender}
            return render(request,"LMSapp/BookIssuedToStudentDetails.html",context)
        else:
            print("Registration Number not Exist")
            return render(request,"LMSapp/BookIssueToStudent.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
@csrf_exempt
def BookSubmitByStudent_Id_Check(request):
    if request.method == 'POST':
        Student_Library_Registration_Number = request.POST['BookSubmitByStudent']
        Data=None
        if Book_Issue_Student.objects.filter(Student_Registration_Number=Student_Library_Registration_Number):
            request.session['Student_Library_Registration_Number'] = Student_Library_Registration_Number
            Data = Book_Issue_Student.objects.filter(Student_Registration_Number=Student_Library_Registration_Number)
        else:
            messages.error(request,"This student has not contain any book")
        return render(request,"LMSapp/BookSubmitByStudent.html",{'Data':Data})
            
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def BookIssueToFaculty_id_check(request):
    if request.method == 'POST':
        Faculty_Library_Registration_Number = request.POST['BookIssueToFaculty']
        if Faculty_Registration.objects.filter(Faculty_Registration_Number=Faculty_Library_Registration_Number):
            print("Faculty Registration Number is exist")
        else:
            print("Faculty Registration Number not Exist")
        return render(request,"LMSapp/BookIssueToFaculty.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def BookSubmitByFaculty_id_check(request):
    if request.method == 'POST':
        Faculty_Library_Registration_Number = request.POST['BookSubmitByFaculty']
        if Faculty_Registration.objects.filter(Faculty_Registration_Number=Faculty_Library_Registration_Number):
            print("Faculty Registration Number is exist")
        else:
            print("Faculty Registration Number not Exist")
        return render(request,"LMSapp/BookIssueToFaculty.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def BookIssueToStudent_BookID(request):
    if request.method == 'POST':
        request.session['fname'] = request.POST['fname']
        request.session['mname'] = request.POST['mname']
        request.session['lname'] = request.POST['lname']
        request.session['Phone1'] = request.POST['Phone1']
        request.session['Phone2'] = request.POST['Phone2']
        request.session['email'] = request.POST['email']
        request.session['city'] = request.POST['city']
        request.session['district'] = request.POST['district']
        request.session['state'] = request.POST['state']
        request.session['pin'] = request.POST['pin']
        request.session['Current_Address'] = request.POST['CurrentAddress']
        request.session['Permanent_Address'] = request.POST['PermanentAddress']
        request.session['Course'] = request.POST['Course']
        request.session['Year'] = request.POST['Year']
        request.session['Branch'] = request.POST['Branch']
        request.session['Gender'] = request.POST['Gender']
        request.session['RegNumber'] = request.POST['regNumber']
        return render(request,"LMSapp/BookIssueToStudent_BookID.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

@csrf_exempt
def BookIssueToStudent_BookIDCheck(request):
    if request.method == 'POST':
        BookId = request.POST['BookIssueToStudent_BookIDCheck']
        if Book_Registration.objects.filter(BookID__iexact=BookId):
            Book = Book_Registration.objects.get(BookID__iexact=BookId)
            
            from datetime import datetime
            currentDT = datetime.now()
            day = str(currentDT.day)
            month = currentDT.strftime("%B")
            year = str(currentDT.year)
            date = day+'/'+month+'/'+year
            
            fname = request.session['fname']
            mname = request.session['mname']
            lname = request.session['lname']
            Phone1 = request.session['Phone1']
            Phone2 = request.session['Phone2']
            email = request.session['email']
            city = request.session['city']
            district = request.session['district']
            state = request.session['state']
            pin = request.session['pin']
            Current_Address = request.session['Current_Address']
            Permanent_Address = request.session['Permanent_Address']
            Course = request.session['Course']
            Year = request.session['Year']
            Branch = request.session['Branch']
            Gender = request.session['Gender']
            RegNumber = request.session['RegNumber']
            
            request.session['BookID'] = Book.BookID
            request.session['BookName'] = Book.BookName
            request.session['Author1'] = Book.Author1
            request.session['Author2'] = Book.Author2
            request.session['Publisher'] = Book.Publisher
            request.session['Page'] = Book.Page
            request.session['Price'] = Book.Price
            request.session['BookBelongsCourse'] = Book.BookBelongsCourse
            request.session['date'] = date
            
            context = {'fname':fname,'mname':mname,'lname':lname,'Phone1':Phone1,'Phone2':Phone2,'email':email,'city':city,'district':district,'state':state,'pin':pin,'Current_Address':Current_Address,'Permanent_Address':Permanent_Address,'Course':Course,'Year':Year,'Branch':Branch,'Gender':Gender,'RegNumber':RegNumber,'BookID':Book.BookID,'BookName':Book.BookName,'Author1':Book.Author1,'Author2':Book.Author2,'Publisher':Book.Publisher,'Page':Book.Page,'Price':Book.Price,'BookBelongsCourse':Book.BookBelongsCourse,'date':date}
            
            return render(request,"LMSapp/BookIssueToStudent_BookID.html",context)
        else:
            messages.error(request,"Book id doesn't exist")
            return render(request,"LMSapp/AdminWelcomePage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def BookIssued(request):
    if request.method == 'POST':
        fname = request.session['fname']
        mname = request.session['mname']
        lname = request.session['lname']
        Phone1 = request.session['Phone1']
        Phone2 = request.session['Phone2']
        email = request.session['email']
        city = request.session['city']
        district = request.session['district']
        state = request.session['state']
        pin = request.session['pin']
        Current_Address = request.session['Current_Address']
        Permanent_Address = request.session['Permanent_Address']
        Course = request.session['Course']
        Year = request.session['Year']
        Branch = request.session['Branch']
        Gender = request.session['Gender']
        RegNumber = request.session['RegNumber']
        
        BookID = request.session['BookID']
        BookName = request.session['BookName']
        Author1 = request.session['Author1']
        Author2 = request.session['Author2']
        Publisher = request.session['Publisher']
        Page = request.session['Page']
        Price = request.session['Price']
        BookBelongsCourse = request.session['BookBelongsCourse']
        date = request.session['date']

        if Book_Issue_Student.objects.filter(BookID__iexact = BookID):
            messages.error(request,"This book id already exist some particular student")
        else:
            Book_Issue_Student(Student_Registration_Number = RegNumber, fname = fname, mname = mname, lname = lname, Phone1 = Phone1, Phone2 = Phone2, email = email, city = city, district = district, state = state, pin = pin, Current_Address = Current_Address, Permanent_Address = Permanent_Address, Course = Course, Year = Year, Branch = Branch, Gender = Gender, BookID = BookID, BookName = BookName, Author1 = Author1, Author2 = Author2, Publisher = Publisher, Page = Page, Price = Price, BookBelongsCourse = BookBelongsCourse, Book_Issue_To_Student_Date = date).save()
            messages.success(request,"Book has successfully issued to student")
        return render(request,"LMSapp/AdminWelcomePage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")

@csrf_exempt
def BookSubmitted(request):
    if request.method == 'POST':
        BookIdSubmission = request.POST['BookIdSubmission']
        Book_Issue_Student.objects.filter(BookID__iexact = BookIdSubmission).delete()
        messages.success(request,'Book has successfully subitted by student')
        return render(request,"LMSapp/AdminWelcomePage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def SubmitAllBooks(request):
    if request.method == 'POST':
        Student_Library_Registration_Number = request.session['Student_Library_Registration_Number']
        Book_Issue_Student.objects.filter(Student_Registration_Number=Student_Library_Registration_Number).all().delete()
        messages.success(request,"This student has submitted all books")
        return render(request,"LMSapp/AdminWelcomePage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
def MainPage(request):
    if request.method == 'POST':
        return render(request,"LMSapp/AdminWelcomePage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")