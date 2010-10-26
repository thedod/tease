#!/usr/bin/python
import os, sys
sys.path.append('/path/to/scripts')
sys.path.append('path/to/scripts/tease_site')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tease_site.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
