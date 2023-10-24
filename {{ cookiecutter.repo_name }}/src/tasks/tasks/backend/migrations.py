import invoke


@invoke.task
def makemigrations(ctx, manage_args=""):
    """
    Create migrations.
    """
    manage_cmd = f"makemigrations {manage_args}"

    cmd = f"python manage.py {manage_cmd}"
    print(cmd)
    ctx.run(cmd, pty=True)
