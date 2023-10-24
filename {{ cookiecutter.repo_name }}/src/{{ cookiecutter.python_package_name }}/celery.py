import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.python_package_name }}.settings.configuration.localhost')

app = Celery('{{ cookiecutter.repo_name }}-worker', broker_url=settings.BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()