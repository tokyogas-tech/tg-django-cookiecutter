import invoke


@invoke.task
def makemigrations(ctx, manage_args=""):
    """
    Create migrations.
    """
    compose_env = f"DJANGO_SETTINGS_MODULE={{ cookiecutter.python_package_name }}.settings.configuration.localhost"
    manage_cmd = f"makemigrations {manage_args}"

    cmd = f"{compose_env} python manage.py {manage_cmd}"
    print(cmd)  # noqa: K104
    ctx.run(cmd, pty=True)
