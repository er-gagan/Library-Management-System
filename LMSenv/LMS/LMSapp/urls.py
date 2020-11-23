from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('AdminLoginPage',views.AdminLoginPage),
    path('StudentLoginPage',views.StudentLoginPage),
    path('AdminWelcomePage',views.AdminWelcomePage),
    path('logout',views.LogOut),
    
    path('StudentRegistrationPage',views.StudentRegistrationPage),
    path('BookIssueToStudent',views.BookIssueToStudent),
    path('BookSubmitByStudent',views.BookSubmitByStudent),
    path('FacultyRegistrationPage',views.FacultyRegistrationPage),
    path('BookIssueToFaculty',views.BookIssueToFaculty),
    path('BookSubmitByFaculty',views.BookSubmitByFaculty),
    path('BookRegistrationPage',views.BookRegistrationPage),
    path('ViewAllBookPage',views.ViewAllBookPage),
    path('ViewBooksByBranch',views.ViewBooksByBranch),
    
    path('Student_Registration_Data',views.Student_Registration_Data),
    path('Book_Registration_Data',views.Book_Registration_Data),
    path('Faculty_Registration_Data',views.Faculty_Registration_Data),
    
    path('BookIssueToStudent_Id_Check',views.BookIssueToStudent_Id_Check),
    path('BookSubmitByStudent_Id_Check',views.BookSubmitByStudent_Id_Check),
    
    path('BookIssueToFaculty_id_check',views.BookIssueToFaculty_id_check),
    path('BookSubmitByFaculty_id_check',views.BookSubmitByFaculty_id_check),
    
    path('BookIssueToStudent_BookID',views.BookIssueToStudent_BookID),
    path('BookIssueToStudent_BookIDCheck',views.BookIssueToStudent_BookIDCheck),
    path('BookIssued',views.BookIssued),
    path('BookSubmitted',views.BookSubmitted),
    path('MainPage',views.MainPage),
    path('SubmitAllBooks',views.SubmitAllBooks),   
]