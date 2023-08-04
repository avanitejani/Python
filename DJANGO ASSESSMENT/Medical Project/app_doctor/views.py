from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random

from .models import *
from app_doctor.models import *
# from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password



# Create your views here.
def doc_index(request):
    return render(request,"doc_index.html")

def doc_register(request):
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
            return render(request,"doc_otp.html")
        else:
            return render(request,"doc_sign-up.html",{"msg":"Paswod And Confirm Password Not Match"})  
    else:    
        return render(request,"doc_sign-up.html")  

def doc_otp(request):    
    if request.method=="POST":
        if otp==int(request.POST["otp"]):
            Doc_user.objects.create(
                name=temp["name"],
                email=temp["email"],
                password=make_password(temp["password"])

            )
            return render(request,"doc_sign-up.html",{"msg":"registation successfull add your information in add doctor "})
        else:
            return render(request,"doc_otp.html",{"msg":"otp not matched"})


    else: 
        return render(request,"doc_sign-up.html",{"msg":"You can not access direct otp please enter correct password and email"})

def doc_login(request):
    if request.method=="POST":
        try:
            User_data = Doc_user.objects.get(email = request.POST["email"])
            if check_password(request.POST["password"],User_data.password):
                request.session["email"]=request.POST["email"]
                return render(request,"doc_index.html")
            else:
                return render(request,"doc_login.html",{"msg":"Password Not Match"})
        except:
            return render(request,"doc_login.html",{"msg":"User not Exist"})
    else:
        return render(request,"doc_login.html")
    
def doc_logout(request):
    del request.session["email"]
    return render(request,"doc_login.html",{"msg":"Logout Successfully"})


# def doc_profile(request):
#     data=Doc_user.objects.get(email=request.session["email"])
#     if request.method=="POST":    
#         try:
#             image_val=request.FILES["propic"]
#         except:
#             image_val=data.propic
#         if request.POST["oldpswd"]:
#             if check_password(request.POST["oldpswd"],data.password):
#                 if request.POST["newpswd"]==request.POST["cnewpswd"]:
#                     data.name=request.POST["name"]
#                     data.password=make_password(request.POST["newpswd"])
#                     data.propic=image_val
#                     data.save()
#                     return render(request,"doc_profile.html",{"data":data,"msg":"Profile Update Succesfully"})
#                 else:
#                     return render(request,"doc_profile.html",{"data":data,"msg":"New Passwrod and New confirm Passwrod not Match"})
#             else:
#                 return render(request,"doc_profile.html",{"data":data,"msg":"Old Passwrod not Match"})
#         else:
#             data.name=request.POST["name"]
#             # data.departments=request.POST["department"]
#             # data.doctor=request.POST["doctor"]
#             data.propic=image_val
#             data.save()
#             return render(request,"doc_profile.html",{"data":data,"msg":"Profile Update Succesfully"})
#     else:
#         return render(request,"doc_profile.html",{"data":data})


def doc_profile(request):
    data=Doc_user.objects.get(email=request.session["email"])
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
                    return render(request,"doc_profile.html",{"data":data,"msg":"Profile Update Succesfully add your data in add doctor"})
                else:
                    return render(request,"doc_profile.html",{"data":data,"msg":"New Passwrod and New confirm Passwrod not Match"})
            else:
                return render(request,"doc_profile.html",{"data":data,"msg":"Old Passwrod not Match"})
        else:
            data.name=request.POST["name"]
            # data.departments=request.POST["department"]
            # data.doctor=request.POST["doctor"]
            data.propic=image_val
            data.save()
            return render(request,"doc_profile.html",{"data":data,"msg":"Profile Update Succesfully you add your data in add doctor"})
    else:
        return render(request,"doc_profile.html",{"data":data})
    
def add_doctor(request):
    doc_data=Doc_user.objects.get(email=request.session["email"])
    if request.method=="POST":
        pass
        Profile.objects.create(
            doc_name=request.POST["dname"],
            # doc_email=request.POST["demail"],
            departments=request.POST["department_typ"],
            doctor=request.POST["doctor_typ"],
            doc_image=request.FILES["d_image"],
            doc_desc=request.POST["doc_desc"],
            doc_id=doc_data

        )
        return render(request,"add_doc.html",{"seller_data":doc_data,"msg":"data added Successfull"})

    else:
        return render(request,"add_doc.html",{"seller_data":doc_data})
        # return render(request,"add_doc.html")



def doc_appointment(request):
    return render(request,"doc_appointment.html")

def doc_about(request):
    return render(request,"doc_about.html")

def doc_service(request):
    return render(request,"doc_service.html")

def doc_services(request):
    return render(request,"doc_services.html")

def doc_gallary(request):
    return render(request,"doc_gallery.html")

def doc_team(request):
    all_doc=Profile.objects.all()
    return render(request,"team.html",{"all_doc":all_doc})
    # return render(request,"doc_team.html")

def doc_blog(request):
    return render(request,"doc_blog.html")

def doc_blogd(request):
    return render(request,"doc_blogd.html")



