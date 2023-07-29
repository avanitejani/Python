from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request,"home.html")

def add_data(request):
    if request.method=="POST":
        User.objects.create(
            #tabale variyabal->  firstname= request.POST[" html-> input vala firstname "],
            firstname=request.POST["firstname"],
            lastname=request.POST["lastname"],
            email=request.POST["email"],
            passowed=request.POST["password"]
        )
        return render(request,"home.html",{"msg":"Dta Added Succesfully"})

    else:
        return render(request,"home.html",{"msg":"Invalid Route"})
    
def show_data(request):
    all_data=User.objects.all()
    return render(request,"table.html",{"all_data":all_data})


def update(request,pk):
    if request.method=="POST":
        one_data=User.objects.get(id=pk)
        one_data.firstname=request.POST["firstname"]
        one_data.lastname=request.POST["lastname"]
        one_data.email=request.POST["email"]
        one_data.passowrd=request.POST["password"]
        one_data.save()
        return show_data(request)
    else:
        one_data=User.objects.get(id=pk)
        return render(request,"update.html",{"one_data":one_data})
     

def delete(request,pk):
    one_data=User.objects.get(id=pk)
    one_data.delete() 
    return show_data(request)
    
    #   get() gives only one add_data
    #   all() gives all add_data   
    #   filter(condition) 