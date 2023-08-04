from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random
# import app_doctor.models import *
from .models import *
# from app_patient.models import *
# from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password



# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        if request.POST["password"]==request.POST["cpassword"]:
            global temp
            temp={ 
            "name":request.POST["name"],
            "email":request.POST["email"],
            "password":request.POST["password"]# pswd =sing-up.html se fild name hai

        }
            global otp
            otp=random.randint(100000,999999)
            subject = 'OTP Verification'
            message = f'Your OTP is. {otp} valid for 5 mintute only'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST["email"], ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,"otp.html")
        else:
            return render(request,"sign-up.html",{"msg":"Paswod And Confirm Password Not Match"})  
    else:    
        return render(request,"sign-up.html")  

def otp(request):    
    if request.method=="POST":
        if otp==int(request.POST["otp"]):
            User.objects.create(
                name=temp["name"],
                email=temp["email"],
                password=make_password(temp["password"])

            )
            return render(request,"sign-up.html",{"msg":"registation successfull"})
        else:
            return render(request,"otp.html",{"msg":"otp not matched"})


    else: 
        return render(request,"sign-up.html",{"msg":"You can not access direct otp please enter correct password and email"})

def login(request):
    if request.method=="POST":
        try:
            User_data = User.objects.get(email = request.POST["email"])
            if check_password(request.POST["password"],User_data.password):
                request.session["email"]=request.POST["email"]
                return render(request,"index.html")
            else:
                return render(request,"login.html",{"msg":"Password Not Match"})
        except:
            return render(request,"login.html",{"msg":"User not Exist"})
    else:
        return render(request,"login.html")
    
def logout(request):
    del request.session["email"]
    return render(request,"login.html",{"msg":"Logout Successfully"})


def profile(request):
    data=User.objects.get(email=request.session["email"])
    if request.method=="POST":    
        try:
            image_val=request.FILES["propic"]
        except:
            image_val=data.propic
        if request.POST["oldpswd"]:
            if check_password(request.POST["oldpswd"],data.password):
                if request.POST["newpswd"]==request.POST["cnewpswd"]:
                    data.name=request.POST["name"]
                    data.password=make_password(request.POST["newpswd"])
                    data.propic=image_val
                    data.save()
                    return render(request,"profile.html",{"data":data,"msg":"Profile Update Succesfully"})
                else:
                    return render(request,"profile.html",{"data":data,"msg":"New Passwrod and New confirm Passwrod not Match"})
            else:
                return render(request,"profile.html",{"data":data,"msg":"Old Passwrod not Match"})
        else:
            data.name=request.POST["name"]
            data.propic=image_val
            data.save()
            return render(request,"profile.html",{"data":data,"msg":"Profile Update Succesfully"})
    else:
        return render(request,"profile.html",{"data":data})



# def show_doctor(request):
#         data=User.objects.get(email=request.session["email"])
        
#         print(all_doc.count())
#         return render(request,"team.html",{"data":data,"all_doc":all_doc})




def appointment(request):
    app=User.objects.get(email=request.session["email"])
    if request.method == 'POST':
        data=Appointment.objects.create(
        name = request.POST['Name'],
        phone = request.POST['Phone'],
        email = request.POST['Email'],
        date = request.POST['Date'],
        department = request.POST['Department'],
        doctor = request.POST['Doctor'],
        messege= request.POST['form_message']
        )
        # time = request.POST['time']

        return render(request, 'appointment.html', {"app":app,"data":data,"msg":"appointment Register Succesfully"})

    else:
        # doctors = Doctor.objects.all()
        return render(request, 'appointment.html', {'app': app})


def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def services(request):
    return render(request,"services.html")

def gallery(request):
    return render(request,"gallery.html")

from app_doctor.models import *

def team(request):
    all_doc=Profile.objects.all()
    return render(request,"team.html",{"all_doc":all_doc})

def blog(request):
    return render(request,"blog.html")

def blogd(request):
    return render(request,"blogd.html")



