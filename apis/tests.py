from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todos.models import Todo

class AccountTests(APITestCase):
    def setUp(self):
        Todo.objects.create(id=4,title='test',description='test')
    def test_create_todo(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('todos-list')
        data = {'title': 'unit test' , 'description':'check if test work well'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_todos_list(self):
        """
        Ensure we can get all records
        """
        url = reverse('todos-list')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_updateEdgeCase_RecordNotExist(self):
        """
        Ensure that we can t update non existing records
        """
        #url = reverse('todos-detail')
        data = {'title': 'unit test' , 'description':'check if test work well'}
        response = self.client.put('apis/v1/todo/5/',data,format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    def test_delete(self):
        """
        ensure that  we can delete content , notice that 204 flag mean that operation succeeded
        """
        url = reverse('todos-detail', kwargs={'pk': 4})
        response = self.client.delete(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

