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
   path('',views.doc_index,name='doc_index'),
   path('doc_register/',views.doc_register,name='doc_register'),
   path('doc_otp/',views.doc_otp,name='doc_otp'),
   path('doc_login/',views.doc_login,name='doc_login'),
   path('doc_logout/',views.doc_logout,name='doc_logout'),
   path('doc_profile/',views.doc_profile,name='doc_profile'),
   path('doc_appointment/',views.doc_appointment,name='doc_appointment'),
   path('doc_about/',views.doc_about,name='doc_about'),
   path('doc_service/',views.doc_service,name='doc_service'),
   path('doc_services/',views.doc_services,name='doc_services'),
   path('doc_gallary/',views.doc_gallary,name='doc_gallary'),
   path('doc_team/',views.doc_team,name='doc_team'),
   path('doc_blog/',views.doc_blog,name='doc_blog'),
   path('doc_blogd/',views.doc_blogd,name='doc_blogd'),
   path('add_doctor/',views.add_doctor,name='add_doctor'),





]