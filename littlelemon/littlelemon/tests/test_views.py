from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from rest_framework.test import APITestCase
import json

#TestCase class
class MenuViewTest (APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Creates common testdata for all testcases
        item1 = MenuItem.objects.create(id=1,title="IceCream", price=80, inventory=100)
        item2 = MenuItem.objects.create(id=2,title="Sushi", price=60, inventory=5100)
        item3 = MenuItem.objects.create(id=3,title="Candy", price=20, inventory=1100)
   
    def test_getall(self):
        response=self.client.get('/api/menu/items')
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content.decode("utf-8"))[0]['title'],'IceCream')  # Check that we got IceCream
        self.assertEqual(len(json.loads(response.content.decode("utf-8"))),3) # And a total of 3

    def test_get_single(self):
        response=self.client.get('/api/menu/2')  # Grab ID 2 - should be Sushi!
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content.decode("utf-8"))['title'],'Sushi')  # Check that we got Sushi
       




       

