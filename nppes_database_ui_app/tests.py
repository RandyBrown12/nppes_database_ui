from django.test import TestCase
from bs4 import BeautifulSoup

# Create your tests here.
class NPPESDatabaseUI(TestCase):
    """
    Verify that the NPPES Database UI renders correctly.
    This test checks the presence of specific elements in the HTML response.
    """
    def test_navbar_text(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        navbar_text = soup.find('div', id='navbar-text')
        self.assertEqual(navbar_text.get_text(strip=True), 'NPPES Database UI')
    
    def test_form_text(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        form_text = soup.find('div', id='form-text')
        self.assertEqual(form_text.get_text(strip=True), 'Search NPPES Database')
