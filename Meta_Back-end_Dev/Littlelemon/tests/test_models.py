# >>>>>>> to run the test: python3 manage.py test tests/

from django.test import TestCase
from restaurant.models import *

class MenuTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(Title='Grilled Fish', Price=13.00, Inventory=25)
        self.assertEqual(item.__str__(), 'Grilled Fish : 13.0')
