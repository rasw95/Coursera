from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name = "index"),
    path('menu/',MenuItemView.as_view()),
    path('menu/<int:pk>', SingleItemView.as_view()),
    path('api-token-auth', obtain_auth_token)
]