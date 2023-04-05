import unittest
from rest_framework.test import *


# Create your tests here.


class Test(unittest.TestCase):
    base_url = 'http://127.0.0.1:8000/api/'

    def test_get_snippet(self):
        client = APIClient()
        client.login(username='admin', password='admin')
        client = RequestsClient()
        response = client.get(self.base_url + 'snippets/')
        assert response.status_code == 200

    def test_delete_snippet(self):
        client = APIClient()
        client.login(username='admin', password='admin')
        response = client.delete(self.base_url + 'snippets/25/')
        assert response.status_code == 204

    def test_put_snippet(self):
        client = APIClient()
        client.login(username='admin', password='admin')
        response = client.put(self.base_url + 'snippets/26/', {'code': '"<?php\r\n echo \"Hi World\""'}, format='json')
        assert response.status_code == 200

    def test_post_snippet(self):
        client = APIClient()
        client.login(username='admin', password='admin')
        response = client.post(self.base_url + 'snippets/', {'code': '"<?php\r\n echo \"Hello World\""'},
                               format='json')
        assert response.status_code == 201
