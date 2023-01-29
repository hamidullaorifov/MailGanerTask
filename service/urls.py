from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^send-email$',views.send_email_page,name='send-email'),
    url(r'^email$',views.email_opened,name='email-opened'),
    
]
