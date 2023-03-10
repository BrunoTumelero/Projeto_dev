"""
WSGI config for client project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import faulthandler
faulthandler.enable()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'client.settings')

application = get_wsgi_application()
