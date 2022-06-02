from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

from .models import Project

# Create your views here.

def projects(request):
    projects = Project.objects.get()
    context = {'projects': projects}
    print(projects)
    return render(request,"dummy.html" , context)

def project(request,pk):
    project_obj = Project.objects.get(id=pk)
    context = {'project':project_obj}
    return render(request,"dummy.html",context) 