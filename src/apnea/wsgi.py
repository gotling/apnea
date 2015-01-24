import os
import sys

project_path = lambda *a: os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), *a)

sys.path[:0] = [project_path('src'),
                project_path('src', 'apps')]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apnea.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()