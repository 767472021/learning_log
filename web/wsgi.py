"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys  # 4

from django.core.wsgi import get_wsgi_application
#from dj_static import Cling
from os.path import dirname, abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))  # 3

sys.path.insert(0, PROJECT_DIR)  # 5
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
application = get_wsgi_application()
