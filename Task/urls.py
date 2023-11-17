from django.urls import path
from .views import TaskCreateApiView, TaskListApiView, TaskRetrieveApiView, TaskUpdateApiView, TaskDeleteApiView

urlpatterns=[
    path('create',TaskCreateApiView.as_view(),name="create"),
    path('list',TaskListApiView.as_view(),name="list"),
    path('task/<int:pk>',TaskRetrieveApiView.as_view(), name="task"),
    path('update/<int:pk>',TaskUpdateApiView.as_view(), name="taskupdate"),
    path('delete/<int:pk>',TaskDeleteApiView.as_view(), name="taskdelete")
]