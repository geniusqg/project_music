#coding=utf-8

import os
import sys
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(dirname(__file__)))
sys.path.insert(0, abspath(join(abspath(dirname(__file__)), '..')))

# django settings
from django.conf import settings
if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "judge.settings")
