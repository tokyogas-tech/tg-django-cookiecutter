import django_webtest


def test_access():
    app = django_webtest.DjangoTestApp()
    response = app.get("/login/")
    assert b"Hello from {{ cookiecutter.service_name }}" in response.content