"""Littlelemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from restaurant import views

# Adding Routers for DRF viewset (Auto establish Get, Post, Update and Delete operations).
#tablesRouter = DefaultRouter()
#menuRouter = DefaultRouter()

#tablesRouter.register(r'tables', views.BookingViewSet)
#menuRouter.register(r'menu', views.MenuItemView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('restaurant.urls')),
    path('api/', include('APIs.urls')),
    #path('api/',include('restaurant.urls')),
    #path('api/booking/',include(tablesRouter.urls)),
    #path('api/',include(menuRouter.urls))
]

