from periban.settings.common import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['137.184.186.235']
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'fcorm.sante@gmail.com'
EMAIL_HOST_PASSWORD = 'Viter280889'