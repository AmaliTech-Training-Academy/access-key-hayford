"""
WSGI config for access_key_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'access_key_manager.settings')

# application = get_wsgi_application()
import os
import sys
from django.core.wsgi import get_wsgi_application

path = 'access-key-hayford/access_key_manager'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'access_key_manager.settings'


application = get_wsgi_application()

