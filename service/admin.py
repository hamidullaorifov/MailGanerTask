# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EmailMessage,Message
# Register your models here.
admin.site.register(EmailMessage)
admin.site.register(Message)