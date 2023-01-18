from django.test import TestCase
<<<<<<< HEAD
import json
from restaurant.models import *
from restaurant.serializers import *
=======
from django.urls import reverse
from restaurant.views import MenuItemView
from restaurant.models import *

>>>>>>> 4042f1f (Switch to SQlite DB / Added Menu routes)

class MenuViewTest(TestCase):
    def setUp(self):
        menu.objects.create(Title='Fish', Price=13.00, Inventory=25)
        menu.objects.create(Title='Sushi', Price=15.00, Inventory=25)
        menu.objects.create(Title='Chiken', Price=14.00, Inventory=25)
<<<<<<< HEAD
        
    def test_get_all(self):
        items = menu.objects.all()
        serializer = MenuSerializer(items, many = True)
        expected =  '[{"Title": "Fish", "Price": "13.00", "Inventory": 25}, {"Title": "Sushi", "Price": "15.00", "Inventory": 25}, {"Title": "Chiken", "Price": "14.00", "Inventory": 25}]'          
        self.assertEqual(json.dumps(serializer.data), expected)
=======

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)
        #items = menu.objects.all()
        #serializer = MenuSerializer(items, many = True)
        #expected =  '[{"Title": "Fish", "Price": "13.00", "Inventory": 25}, {"Title": "Sushi", "Price": "15.00", "Inventory": 25}, {"Title": "Chiken", "Price": "14.00", "Inventory": 25}]'          
        #self.assertEqual(json.dumps(serializer.data), expected)
>>>>>>> 4042f1f (Switch to SQlite DB / Added Menu routes)
