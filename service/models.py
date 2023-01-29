# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User,models.CASCADE,related_name='messages')
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
class EmailMessage(models.Model):
    message = models.ForeignKey(Message,on_delete=models.CASCADE)
    email = models.EmailField()
    opened = models.BooleanField(default=False)

    def __str__(self):
        return self.email
