from django.db import models

class Task(models.Model):
    body = models.CharField(max_length=128)
