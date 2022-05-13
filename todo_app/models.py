from django.db import models

# Create your models here.
class Task(models.Model):
    '''creating the task table in my database'''
    name = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    