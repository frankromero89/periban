from periban.settings.common import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['elperiban.com']
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('DJANGO_SENDERS_MAIL')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_SENDERS_MAIL_PSWD')