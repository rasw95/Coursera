from django.test import TestCase
import json
from restaurant.models import *
from restaurant.serializers import *

class MenuViewTest(TestCase):
    def setUp(self):
        menu.objects.create(Title='Fish', Price=13.00, Inventory=25)
        menu.objects.create(Title='Sushi', Price=15.00, Inventory=25)
        menu.objects.create(Title='Chiken', Price=14.00, Inventory=25)
        
    def test_get_all(self):
        items = menu.objects.all()
        serializer = MenuSerializer(items, many = True)
        expected =  '[{"Title": "Fish", "Price": "13.00", "Inventory": 25}, {"Title": "Sushi", "Price": "15.00", "Inventory": 25}, {"Title": "Chiken", "Price": "14.00", "Inventory": 25}]'          
        self.assertEqual(json.dumps(serializer.data), expected)