from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class ProductTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_product_list_is_avaliable(self):
        url = reverse('product_list:product_category', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_create_is_avaliable(self):
        url = reverse('product_detail:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
