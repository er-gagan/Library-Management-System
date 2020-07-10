from django.shortcuts import render
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
