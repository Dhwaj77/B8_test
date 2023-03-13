from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.

# views
    # - class based view
    # - function based view


# def welcome(request):             # request is a reserved keyword, ye jo request hai wo hamari http request hai
    # print(request.method)
    # print(request.user)
    # print(request.__dict__)
    # print(request.GET.get("name"))      # clientsite se server site me access kr sakte hai
    # print(request.GET["age"])             # age mil jayega
    # print(type(request.GET["age"]))   # type is str
    # print(request.GET)                         #http://127.0.0.1:8000/home/?name=abc&surname=pqr&age=26 
    
    # stud = Student.objects.values("name")
    # final_stud = list(map(lambda x:x['name'],stud))
    # return HttpResponse(f"Welcome to Django Application...!!!{final_stud}")

def welcome(request):
    return render(request,"home.html")