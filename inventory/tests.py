from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import LocationMaster, CategoryMaster, ItemMaster, InventoryStockMaster
 
class APITest(APITestCase):
    fixtures = ['location_master_fixture.json', 'category_master_fixture.json', 
                'item_master_fixture.json', 'inventory_stock_master_fixture.json']
 
    def setUp(self):
        # # Create a user for authentication if needed
        # # self.user = User.objects.create_user(username='testuser', password='test#123')
        # # self.client.login(username='testuser', password='testpassword'
        # pass
        self.user = User.objects.get(username='srinath.k')
        self.client.login(username='srinath.k', password='admin@123')
 
    # LocationMaster API Tests
    def test_create_location(self):
        response = self.client.post('/inventory/locations/', {'location_name': 'New Delhi'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
    def test_get_location(self):
        response = self.client.get('/inventory/locations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_update_location(self):
        response = self.client.patch('/inventory/locations/1/', {'location_name': 'New Delhi','status': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_delete_location(self):
        response = self.client.delete('/inventory/locations/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 
 
    # CategoryMaster API Tests
    def test_create_category(self):
        response = self.client.post('/inventory/categories/', {'category_name': 'Electronics','status': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
    def test_get_category(self):
        response = self.client.get('/inventory/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_update_category(self):
        response = self.client.patch('/inventory/categories/1/', {'category_name': 'Home Appliances','status': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_delete_category(self):
        response = self.client.delete('/inventory/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 
 
    # ItemMaster API Tests
    def test_create_item(self):
        response = self.client.post('/inventory/itemmasters/', {
            'item_code': 'ITM/2024/XYZ',
            'item_name': 'Sample Item',
            'item_file': 'path/to/astro.jpg',
            'specification': 'Spec Details',
            'category_id': 1,
            'status': 1
           
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
    def test_get_item(self):
        response = self.client.get('/inventory/itemmasters/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_update_item(self):
        response = self.client.patch('/inventory/itemmasters/1/', {'item_name': 'Updated Item Name'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_delete_item(self):
        response = self.client.delete('/inventory/itemmasters/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 
    # InventoryMaster API Tests
    def test_create_inventory_stock(self):
        response = self.client.post('/inventory/inventorymasters/', {
            'item_var_id': 1,
            'location_id': 1,
            'quantity': 100,
            'batch_no': 'BATCH1234',
            'inventory_type': 'add_invent',
            'item_type': 'finished',
            'inventory_code': 'FGBU84555325',
            'quantity_type':'Box',
            'status': 1
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
    def test_get_inventory_stock(self):
        response = self.client.get('/inventory/inventorymasters/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_update_inventory_stock(self):
        response = self.client.patch('/inventory/inventorymasters/1/', {'quantity': 150}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_delete_inventory_stock(self):
        response = self.client.delete('/inventory/inventorymasters/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)