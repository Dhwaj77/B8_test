from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register([Person, College, Principal, Department, Student, Subject]) 