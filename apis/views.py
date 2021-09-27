from rest_framework import generics
from rest_framework import viewsets
from todos import models
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class TodoReverse(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    def get_queryset(self):
       queryset = models.Todo.objects.all().order_by("-id")
       return queryset

'''

from rest_framework import generics

from todos import models
from .serializers import TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
'''
