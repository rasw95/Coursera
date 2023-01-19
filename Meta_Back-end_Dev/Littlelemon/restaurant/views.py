# from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
import json
import datetime
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):   # Using FormModel method.
    #form = BookingForm()
    #if request.method == 'POST':
       # form = BookingForm(request.POST)
        #if form.is_valid():
            #form.save()
    #context = {'form':form}
    return render(request, 'book.html', {})

# Add your code here to create new views
def menu(request):
    menu_model = MenuItem.objects.all().order_by('name')
    menu_data = { 'menu': menu_model }
    return render(request, 'menu.html', menu_data)

def display_items(request, pk = None):

    if pk:
        item = MenuItem.objects.get( pk = pk)
    else:
        item = ''

    item_data = { 'item': item}
    return render(request, 'menu_item.html', item_data)

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
            return JsonResponse({"status":"ok"})
        else:
            return HttpResponse("{'error 1': 'Book_request_already_taken.'}", content_type='application/json')
    
    date = request.GET.get('date',datetime.date.today())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')



