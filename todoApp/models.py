from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=50)

# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=70)
    note = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, default=None)


