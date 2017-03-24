from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=70)
    note = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    manager = models.CharField(max_length=20)
    # parent_group = models.ForeignKey('self', blank=True, null=True)
    parent_group = models.CharField(max_length=20, default='AWARE')
    contact = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=30)
