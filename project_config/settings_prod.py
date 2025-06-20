"""
Production settings for project_config project.
Import from settings.py and override only what's needed.
"""
from .settings import *

DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

# Add any production-specific settings
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
