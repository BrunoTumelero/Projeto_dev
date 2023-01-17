from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from client.login import urls as login_urls
from client.public import urls as public_urls
from client.consumer import urls as consumer_urls
from client.company import urls as company_urls

urlpatterns = [
    url(r'^login/', include(login_urls, namespace='login')),
    url(r'^public/', include(public_urls, namespace='public')),
    url(r'^consumer/', include(consumer_urls, namespace='consumer')),
    url(r'^company/', include(company_urls, namespace='company')),
]
