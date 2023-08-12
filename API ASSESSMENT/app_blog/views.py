from django.shortcuts import render
from django.shortcuts import render
from .models import Blog

from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_blog.models import Blog
from app_blog.serializers import BlogSerializer

import datetime
# import time
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        Blog.objects.create(
            titel=request.POST["titel"],
            content=request.POST["content"],
            created_at=datetime.datetime.now(),
            Update=datetime.datetime.now()
        )
        return render(request, "index.html", {"msg": "Data Added  Succesfully."})
    else:
        return render(request, 'index.html')
    
@api_view(['GET'])
def all_data(request):
    data=Blog.objects.all()
    serial=BlogSerializer(data,many=True)
    return Response(serial.data)

@api_view(['GET'])
def one_data(request,pk):
    ony_data=Blog.objects.get(id=pk)
    serial=BlogSerializer(ony_data)
    return Response(serial.data)

@api_view(['GET'])
def update(request,pk,B,C):
    try:
        one_data=Blog.objects.get(id=pk)
        one_data.Blog=B
        one_data.Contant=C
        one_data.save()

    except:
        Blog.objects.create(
            Blog=B,
            Contant=C
        )
    data=Blog.objects.all()
    serial=BlogSerializer(data,many=True)
    return Response(serial.data)

@api_view(['GET'])
def delete(request,pk):
    one_delete=Blog.objects.get(id=pk)
    one_delete.delete()
    one_delete.save()
    serial=BlogSerializer(one_delete,many=True)
    return Response(serial.data)
    
