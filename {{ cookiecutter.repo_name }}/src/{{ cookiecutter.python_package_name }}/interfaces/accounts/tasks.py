from django.core import mail
from {{ cookiecutter.python_package_name }}.celery import app


@app.task()
def test_tasks(email: str):
    mail.send_mail(
        "test",
        "message",
        "info@{{ cookiecutter.repo_name }}.com",
        [email],
    )
