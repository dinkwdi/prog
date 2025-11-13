from django.test import TestCase
from django.urls import reverse

class SimpleViewTest(TestCase):
    def test_partner_list_view(self):
        """Проверка что страница с партнерами открывается"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class SaleViewTest(TestCase):
    def test_sale_list_view(self):
        """Проверка что страница с продажами открывается"""
        response = self.client.get(reverse('sale'))
        self.assertEqual(response.status_code, 200)

class CreatePartnerViewTest(TestCase):
    def test_create_partner_view(self):
        """Проверка что страница с добавлением партнеров открывается"""
        redponse = self.client.get(reverse('create'))
        self.assertEqual(redponse.status_code, 200)

class CreateSaleViewTest(TestCase):
    def test_create_sale_view(self):
        """Проверка что страница с партнерами открывается"""
        response = self.client.get(reverse('sale-create'))
        self.assertEqual(response.status_code, 200)