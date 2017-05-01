from django.test import TransactionTestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from accounts.models import User


class UserViewSetTests(TransactionTestCase):

    def setUp(self):
        self.client = APIClient()
        self.path = '/api/v1/users'
        self.user = User.objects.create_user(username='test user')
        self.token = Token.objects.create(user=self.user)
        self.key = 'Token ' + self.token.key

    def test_create(self):
        # Test new token.
        response = self.client.post(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get('token'))

        # Test Authorized response.
        self.client.credentials(HTTP_AUTHORIZATION=self.key)
        response = self.client.post(self.path)
        self.assertEqual(response.status_code, 403)

    def test_destroy(self):
        # Test authorized delete.
        self.client.credentials(HTTP_AUTHORIZATION=self.key)
        response = self.client.delete(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(id=self.user.pk).exists())
        self.assertFalse(Token.objects.filter(key=self.token.key))

        # Test unauthorized delete.
        self.client.credentials()
        response = self.client.delete(self.path)
        self.assertEqual(response.status_code, 400)
