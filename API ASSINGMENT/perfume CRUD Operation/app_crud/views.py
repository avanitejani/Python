from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from .models import Perfume

from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_crud.models import Perfume
from app_crud.serializers import PerfumeSerializer

import datetime
# import time
from django.shortcuts import render
from .models import *


# pip install djangorestframework

# Create your views here.
def index(request):
    if request.method == "POST":
        Perfume.objects.create(
            name=request.POST["name"],
            brand=request.POST["brand"],
            notes=request.POST["notes"],
            price=request.POST["price"],
            created_at=datetime.datetime.now(),
            Update=datetime.datetime.now()



        )
        return render(request, "index.html", {"msg": "Data Added  Succesfully."})
    else:
        return render(request, 'index.html')
    
@api_view(['GET'])
def all_data(request):
    data=Perfume.objects.all()
    serial=PerfumeSerializer(data,many=True)
    return Response(serial.data)

@api_view(['GET'])
def one_data(request,pk):
    ony_data=Perfume.objects.get(id=pk)
    serial=PerfumeSerializer(ony_data)
    return Response(serial.data)

@api_view(['GET'])
def update(request,pk,A,B,C,D):
    try:
        one_data=Perfume.objects.get(id=pk)
        one_data.name=A
        one_data.brand=B
        one_data.notes=C
        one_data.price=D

        one_data.save()

    except:
        Perfume.objects.create(
            name=A,
            brand=B,
            notes=C,
            price=D
        )
    data=Perfume.objects.all()
    serial=PerfumeSerializer(data,many=True)
    return Response(serial.data)

@api_view(['GET'])
def delete(request,pk):
    one_delete=Perfume.objects.get(id=pk)
    one_delete.delete()
    one_delete.save()
    serial=PerfumeSerializer(one_delete,many=True)
    return Response(serial.data)
    
