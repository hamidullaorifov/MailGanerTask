# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .tasks import send_email_task
from django.views.decorators.csrf import csrf_exempt
from .models import Message,EmailMessage
from json import loads

User = get_user_model()

@login_required
def index(request):
    user = request.user
    messages = Message.objects.filter(sender=user)
    email_messages = EmailMessage.objects.filter(message__in=messages)
    context = {
        'emails':email_messages
    }
    return render(request,'service/index.html',context)


@csrf_exempt
def email_opened(request):
    body = request.body
    data = loads(body)
    id = data['id']
    email = data['email']
    message = Message.objects.get(id=id)
    email_message = EmailMessage.objects.get(message=message,email=email)
    email_message.opened=True
    email_message.save()
    return JsonResponse({"opened":True})




@login_required
def send_email_page(request):
    if request.method=='POST':
        data = request.POST
        title = data['title']
        body = data['message']
        user = request.user
        message = Message.objects.create(sender=user,body=body,title=title)
        receivers = User.objects.exclude(id=user.id).values('email')
        receivers_emails_list = [r['email'] for r in receivers]     
        send_email_task.delay(message.id,title,body,receivers_emails_list,user.email)
        return redirect('index')
    return render(request,'service/send-email.html')
