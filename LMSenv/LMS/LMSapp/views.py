from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"LMSapp/home.html")

def AdminLoginPage(request):
    return render(request,"LMSapp/AdminLoginPage.html")

def StudentLoginPage(request):
    return render(request,"LMSapp/StudentLoginPage.html")
        