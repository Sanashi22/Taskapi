from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView

# Create your views here.

class TaskCreateApiView(CreateAPIView):
    queryset= Task.objects.all()
    serializer_class= TaskSerializer

class TaskListApiView(ListAPIView):
    queryset= Task.objects.all()
    serializer_class= TaskSerializer

class TaskRetrieveApiView(RetrieveAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class TaskUpdateApiView(UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class TaskDeleteApiView(DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
