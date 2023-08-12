"""
URL configuration for pro_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from.import views

urlpatterns = [
   path('',views.index,name='index'),
   path('register/',views.register,name='register'),
   path('otp/',views.otp,name='otp'),
   path('login/',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
   path('profile/',views.profile,name='profile'),
   path('appointment/',views.appointment,name='appointment'),
   path('about/',views.about,name='about'),
   path('service/',views.service,name='service'),
   path('services/',views.services,name='services'),
   path('gallery/',views.gallery,name='gallery'),
   path('team/',views.team,name='team'),
   path('doc_info/<int:pk>',views.doc_info,name='doc_info'),


   path('blog/',views.blog,name='blog'),
   path('blogd/',views.blogd,name='blogd'),
#    path('show_doctor/',views.show_doctor,name='show_doctor'),





]