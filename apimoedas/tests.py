from django.test import TestCase
from django.urls import reverse


class Api_moedas_Test(TestCase):
    def test_url_home(self):
        '''Testa se a url inicial é / ou se mudou'''
        home_url = reverse('apimoedas:precos')
        self.assertEqual(home_url, '/api/v1/precos/')


    def test_view_home_is_ok(self):
        home_url = reverse('apimoedas:precos')
        response = self.client.get(home_url)
        self.assertEqual(response.status_code, 200)
