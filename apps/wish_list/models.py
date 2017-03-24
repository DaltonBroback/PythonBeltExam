from __future__ import unicode_literals
from django.db import models
from ..loginregistration.models import User
# from django.db import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    user = models.ManyToManyField(User, related_name="items")
    added_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
