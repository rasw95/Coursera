from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.
def index (request):
    return render(request, 'index.html', {})

@permission_classes([IsAuthenticated])
class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

@permission_classes([IsAuthenticated])
class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer

