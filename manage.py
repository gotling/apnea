#!/usr/bin/env python
import os
import sys

project_path = lambda *a: os.path.join(os.path.dirname(__file__), *a)

if __name__ == "__main__":
    sys.path[:0] = [project_path('src'),
                    project_path('src', 'apps')]

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apnea.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)