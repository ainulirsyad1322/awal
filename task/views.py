from django.http import request
from . import models
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.POST:
        username = request.POST['username']
        print(username)
        pwd = request.POST['pasword'] 
        print(pwd)
        models.tugas.objects.create(name = username, password = pwd)

    data = models.tugas.objects.all()
    return render(request,'index.html',{
        'data' : data,
    })

def update(request, id):
    if request.POST:
        new_name= request.POST['username']
    models.tugas.objects.filter (pk=id).update(name = new_name)
    redirect('/') 


    return render(request, 'update.html')   
    
def ainul(request):
    return render(request,'ainul.html')