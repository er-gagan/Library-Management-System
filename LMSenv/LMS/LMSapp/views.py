from django.shortcuts import redirect, render
from django.http import HttpResponse
from LMSapp.models import Student_Registration,Faculty_Registration,Book_Registration

# username contact@rbmi
# pwd contact@rbmi

def home(request):
    return render(request,"LMSapp/home.html")

def AdminLoginPage(request):
    return render(request,"LMSapp/AdminLoginPage.html")

def StudentLoginPage(request):
    return render(request,"LMSapp/StudentLoginPage.html")

def AdminWelcomePage(request):
    if request.method == 'POST':
        return render(request,"LMSapp/AdminWelcomePage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
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
        Current_Address = request.POST['CurrentAddress']
        Permanent_Address = request.POST['PermanentAddress']
        Course = request.POST['Course']
        Year = request.POST['Year']
        Branch = request.POST['Branch']
        Gender = request.POST['Gender']
        Student_Registration(fname = fname,mname = mname,lname = lname,Phone1 = Phone1,Phone2 = Phone2,email = email,city = city,district = district,state = state,pin = pin,Current_Address = Current_Address,Permanent_Address = Permanent_Address,Course = Course,Year = Year,Branch = Branch,Gender = Gender).save()
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
        Faculty_Registration(fname = fname,mname = mname,lname = lname,Phone1 = Phone1,Phone2 = Phone2,email = email,city = city,district = district,state = state,pin = pin,Current_Address = Current_Address,Permanent_Address = Permanent_Address,Branch = Branch,Gender = Gender).save()
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
    
def BookSubmitByStudent_Id_Check(request):
    if request.method == 'POST':
        Student_Library_Registration_Number = request.POST['BookSubmitByStudent']
        if Student_Registration.objects.filter(Student_Registration_Number=Student_Library_Registration_Number):
            Student_data = Student_Registration.objects.get(Student_Registration_Number=Student_Library_Registration_Number)
            print(Student_data.fname,Student_data.mname,Student_data.lname,Student_data.Phone1,Student_data.Phone2,Student_data.email,Student_data.city,Student_data.district,Student_data.state,Student_data.pin,Student_data.Current_Address,Student_data.Permanent_Address,Student_data.Course,Student_data.Year,Student_data.Branch,Student_data.Gender)
        else:
            print("Registration Number not Exist")
        return render(request,"LMSapp/BookSubmitByStudent.html")
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
        return render(request,"LMSapp/BookIssueToStudent_BookID.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
    
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
            
            print(Book.BookID,Book.BookName,Book.Author1,Book.Author2,Book.Publisher,Book.Page,Book.Price,Book.BookBelongsCourse,date)
            print("Book Issued To Student")
        else:
            print("Book ID Not Exist")
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")