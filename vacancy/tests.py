from django.test import Client, TestCase


class TestHomePage(TestCase):

    def test_home_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
