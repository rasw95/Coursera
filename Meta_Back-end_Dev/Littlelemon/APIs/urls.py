from django.urls import path 
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('groups/manager/users/', ManagerView.as_view()),
    path('groups/manager/users/<int:pk>', ManagerView.as_view()),
    path('menu-items/', MenuItemView.as_view({'get':'list'})),
    path('menu-items/<int:pk>', SingleItemView.as_view()),
]
   