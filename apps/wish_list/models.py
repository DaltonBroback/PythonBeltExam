from __future__ import unicode_literals
from django.db import models
# from apps.loginregistration.models import User
# from django.db import User

class Item(models.Model):
    item = models.CharField(max_length=255)
    user = models.ForeignKey('loginregistration.User', related_name="item")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
