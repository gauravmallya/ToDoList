from django.urls import re_path
from ToDoApp import views

urlpatterns=[
    re_path(r'^task/$', views.taskAPI),
    re_path(r'^task/([0-9]+)$', views.taskAPI)
]