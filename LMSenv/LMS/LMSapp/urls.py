from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('AdminLoginPage',views.AdminLoginPage),
    path('StudentLoginPage',views.StudentLoginPage),
    path('AdminWelcomePage',views.AdminWelcomePage),
    
    path('StudentRegistrationPage',views.StudentRegistrationPage),
    path('BookIssueToStudent',views.BookIssueToStudent),
    path('BookSubmitByStudent',views.BookSubmitByStudent),
    path('FacultyRegistrationPage',views.FacultyRegistrationPage),
    path('BookIssueToFaculty',views.BookIssueToFaculty),
    path('BookSubmitByFaculty',views.BookSubmitByFaculty),
    path('BookRegistrationPage',views.BookRegistrationPage),
    path('ViewAllBookPage',views.ViewAllBookPage),
    path('ViewBooksByBranch',views.ViewBooksByBranch),
]