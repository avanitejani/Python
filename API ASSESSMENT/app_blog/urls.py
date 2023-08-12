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
# 
urlpatterns = [
   path('',views.index,name='index'),


    #  path('', views.home, name='home'),
    path('all_data/', views.all_data),
    path('one_data/<int:pk>', views.one_data),
    path('update/<int:pk>/<str:B>/<str:C>', views.update),
    path('delete/<int:pk>', views.delete),

]