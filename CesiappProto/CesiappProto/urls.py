"""
URL configuration for CesiappProto project.

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
from django.contrib import admin
from django.urls import path
from Cesiapp.views import index, type_place_list, update_places

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('ParkingPlace/', type_place_list, name='type_place_list'),
    path('update_places/<int:pk>/<str:action>/', update_places, name='update_places'),
]
