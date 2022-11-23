from utils.tests import BaseTestCase
from django.urls import reverse
import json
class AccountsTest(BaseTestCase):    
    def test_login_fail(self):
        self.assertNotEqual(self.login('dada', 'asdasd').status_code, 200)
    
    def test_login_client(self):
        self.assertEqual(self.login('client@gmail.com', 'ynwa2684').status_code, 200)
    
    def test_login_superuser(self):
        self.assertEqual(self.login('super@gmail.com', 'ynwa2684').status_code, 200)
    
    def test_clients_list(self):
        self.assertEqual(self.get_from_path_name('clients').status_code, 200)

    def test_signup(self):
        response = self.post_json(
            reverse('signup'),
            {
                'email': 'test@test.com',
                'username': 'test',
                'password': 'password',
            },
        )
        
        self.assertEqual(response.status_code, 201)
