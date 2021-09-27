from django.urls import path

#from .views import ListTodo, DetailTodo
from .views import TodoViewSet ,TodoReverse
from rest_framework.routers import DefaultRouter

urlpatterns = [
    #path('', ListTodo.as_view()),
    #path('<int:pk>/', DetailTodo.as_view()),
]

router = DefaultRouter()
router.register('todo', TodoViewSet, basename='todos')
router.register('reverse',TodoReverse,basename='reverse')
urlpatterns = router.urls
