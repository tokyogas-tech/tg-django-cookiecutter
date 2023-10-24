from django.apps import AppConfig


class Config(AppConfig):
    name = "{{ cookiecutter.python_package_name }}.interface.accounts"
    label = "accounts"
