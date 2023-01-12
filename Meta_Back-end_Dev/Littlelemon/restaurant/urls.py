from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name = "index"),
    path('api-token-auth', obtain_auth_token)
]