from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import EmailMessage,Message











@shared_task
def send_email_task(id,title,body,receivers,sender):
    subject = title
    from_email = 'From '+sender
    message = Message.objects.get(id=id)
    for receiver in receivers:
        context={
            'receiver':receiver,
            'message':body,
            'sender':sender,
            'message_id':id,
        }
        
        EmailMessage.objects.create(message=message,email=receiver)
        html_message = render_to_string('service/email-template.html', context=context)
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, from_email, [receiver], html_message=html_message,fail_silently=True)
    return "done"