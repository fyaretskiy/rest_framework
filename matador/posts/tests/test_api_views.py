from unittest.mock import Mock, patch

from django.test import TransactionTestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from accounts.models import User

from ..models import Post


class PostViewSetTests(TransactionTestCase):

    def setUp(self):
        self.post_id = 1

        self.client = APIClient()
        self.path = '/api/v1/posts/{}'.format(self.post_id)
        self.user = User.objects.create_user(username='test user')
        self.token = Token.objects.create(user=self.user)
        self.key = 'Token ' + self.token.key

    @patch('posts.models.requests.get')
    def test_retrieve_db_call(self, get):
        Post.objects.create(user=self.user, data_user_id=1,
                            data_post_id=self.post_id)
        self.client.credentials(HTTP_AUTHORIZATION=self.key)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data_post_id'], self.post_id)
        self.assertFalse(get.called)

    @patch('posts.models.requests.get')
    def test_retrieve_api_call(self, get):
        return_value = [{'userId': 1, 'id': 1, 'title': 'title',
                         'body': 'body'}]

        mock_obj = Mock()
        mock_obj.json.return_value = return_value
        get.return_value = mock_obj

        self.client.credentials(HTTP_AUTHORIZATION=self.key)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data_post_id'], self.post_id)
        self.assertTrue(Post.objects.filter(data_post_id=self.post_id))

    def test_retrieve_not_authenticated(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 401)
