from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = "index"),
    path('menu/',MenuItemView.as_view()),
    path('menu/<int:pk>', SingleItemView.as_view()),
]