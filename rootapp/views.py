from django.shortcuts import render
from .models import *

# Create your views here.


def kurs(request):
    kurs = Kurs.objects.all()
    print(kurs)
    context = {'kurs': kurs}

    return render(request, 'kurs.html',context=context)


def students(request):

    students = Student.objects.all()

    context = {'students': students}

    return render(request,'student.html')
