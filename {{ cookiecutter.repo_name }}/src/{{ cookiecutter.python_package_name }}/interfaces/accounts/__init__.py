from django.apps import AppConfig


class Config(AppConfig):
    name = "{{ cookiecutter.python_package_name }}.interfaces.accounts"
    label = "accounts"
