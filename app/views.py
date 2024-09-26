from django.shortcuts import render

# Create your views here.
from app.models import * 
from django.http import HttpResponse

def insert_Dept(request):
    Dept_name=input('Enter Dept_name')
    Dept_id=input('Enter a Dept_id')
    Dept_loc=input('Enter a Dept_loc')
    DO=Dept.objects.get_or_create(Dept_name=Dept_name)
    if DO[1]:
        return HttpResponse('New object is created')
    else:
        return HttpResponse('user objecct is already exists')  
