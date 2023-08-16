# from rest_framework import serializers
# from .models import *

# class BlogSerializer(serializers.ModelSerializer):

#     class Meta:

#         model  =  Blog
#         fields  = '__all__'

from rest_framework import serializers
# from .models import *
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'