# coding: utf-8

from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import Task
from .serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
