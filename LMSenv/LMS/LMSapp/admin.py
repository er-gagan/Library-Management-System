from django.contrib import admin
from LMSapp.models import Book_Issue_Student, Student_Registration,Faculty_Registration,Book_Registration
# Register your models here.
admin.site.register((Student_Registration,Faculty_Registration,Book_Registration,Book_Issue_Student))