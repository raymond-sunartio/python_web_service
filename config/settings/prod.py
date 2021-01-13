import os

from .base import *  # noqa: F401, F403

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = True
