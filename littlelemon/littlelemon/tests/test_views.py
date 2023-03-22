from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from rest_framework.test import APITestCase
import json

#TestCase class
class MenuViewTest (APITestCase):
    def setUp(self):
        item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        item2 = MenuItem.objects.create(title="Sushi", price=60, inventory=5100)
        item3 = MenuItem.objects.create(title="Candy", price=20, inventory=1100)
   
    def test_getall(self):
        response=self.client.get('/restaurant/menu/items')
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content.decode("utf-8"))[0]['title'],'IceCream')

       

