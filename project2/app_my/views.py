from django.shortcuts import render
from .models import *
from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request,"form.html")

def add_data(request):
    if request.method=="POST":
        User.objects.create(
            salutation=request.POST["salutation"],
            firstname=request.POST["firstName"],
            lastname=request.POST["lastName"],
            gender=request.POST["gender"],
            email=request.POST["email"],
            dob=request.POST["birthDate"],   
            address=request.POST["address"],
            # language=request.POST["language"]
            )
        return render(request,"form.html",{"msg":"Data Added Succesfully"})

    else:
        return render(request,"form.html",{"msg":"Invalid Route"})
    
# def checkbox(request):
#     if request.method == 'POST':
#         c = request.POST.get('c')
#         cc = request.POST.get('c++')
#         java = request.POST.get('java')
#         python = request.POST.get('python')
#         print(f'{c}{cc}{java}{python})

#     return render(request, 'form.html')

def checkbox(request):
    if request.method == 'POST':
        checkbox_values = request.POST.getlist('checkbox_values')
        print(checkbox_values)  # Example: ['value1', 'value3']
        # Your code logic here
    return render(request, 'from.html')


#     1---Create a Environment
# python -m venv environementname
# python -m venv myenv

# 2----Activate your environementname 
# environementname\Scripts\activate 
# myenv\Scripts\activate


# 3----installing Djnago
# pip install django 

# 4--- craeting project
# django-admin startproject projectname .
# django-admin startproject ecommerce .

# 5----creating application
# django-admin startapp appname
# django-admin startapp app_crud

# 6--creating datatbase

# python manage.py makemigrations
# python manage.py migrate

# 7---running your project
# python manage.py runserver

# 8--linking app with project
# goto settings.py file inside project folder

# goto installed_apps section and add our appname

# jinja--python code in html
    