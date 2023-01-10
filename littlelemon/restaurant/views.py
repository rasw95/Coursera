# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_model = Menu.objects.all().order_by('name')
    menu_data = { 'menu': menu_model }
    return render(request, 'menu.html', menu_data)

def display_items(request, pk = None):

    if pk:
        item = Menu.objects.get( pk = pk)
    else:
        item = ''

    item_data = { 'item': item}
    return render(request, 'menu_item.html', item_data)



