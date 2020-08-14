from django.shortcuts import render
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