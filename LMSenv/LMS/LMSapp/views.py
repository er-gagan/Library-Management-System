from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
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
        Current_Address = request.POST['Current_Address']
        Permanent_Address = request.POST['Permanent_Address']
        print(fname,mname,lname,Phone1,Phone2,email,city,district,state,pin,Current_Address,Permanent_Address)
        return render(request,"LMSapp/StudentRegistrationPage.html")
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")