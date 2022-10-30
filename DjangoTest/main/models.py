from unittest.util import _MAX_LENGTH
from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return str(self.text)