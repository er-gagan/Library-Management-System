from django.contrib import admin
from LMSapp.models import Student_Registration,Faculty_Registration,Book_Registration
# Register your models here.
admin.site.register((Student_Registration,Faculty_Registration,Book_Registration))