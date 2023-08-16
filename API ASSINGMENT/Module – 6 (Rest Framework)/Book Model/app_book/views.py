from django.shortcuts import render
from django.shortcuts import render
from .models import Book

from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_book.models import Book
from app_book.serializers import BookSerializer

# import datetime
# import time
from django.shortcuts import render
from .models import *


# pip install djangorestframework
# from rest_framework import serializers
      
# Create your views here.


def index(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["titel"],
            author=request.POST["author"],
            isbn=request.POST["isbn"],
            publisher=request.POST["publisher"],

            # created_at=datetime.datetime.now(),
            # Update=datetime.datetime.now()
        )
        return render(request, "index.html", {"msg": "Data Added  Succesfully."})
    else:
        return render(request, 'index.html')
    
@api_view(['GET'])
def all_data(request):
    data=Book.objects.all()
    serial=BookSerializer(data,many=True)
    return Response(serial.data)

@api_view(['GET'])
def one_data(request,pk):
    ony_data=Book.objects.get(id=pk)
    serial=BookSerializer(ony_data)
    return Response(serial.data)




# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

