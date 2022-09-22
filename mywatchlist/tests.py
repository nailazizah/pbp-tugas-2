from django.test import TestCase, Client
from django.urls import resolve


# Create your tests here.
class test_url(TestCase):
    def test_url_html(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_url_xml(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
