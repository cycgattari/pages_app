from django.test import SimpleTestCase

# Create your tests here.

class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) # code 200 means that HTTP OK
# successfull http request.
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
