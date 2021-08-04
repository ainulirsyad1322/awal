from django.shortcuts import render

# Create your views here.
def index(request):
    if request.POST:
        username = request.POST['username']
        print(username)
        pasword = request.POST['pasword'] 
        print(pasword)   
    return render(request,'index.html')
    
def ainul(request):
    return render(request,'ainul.html')
