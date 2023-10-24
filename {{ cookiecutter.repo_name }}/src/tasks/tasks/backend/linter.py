from invoke.tasks import task

from tasks import constants


@task
def run_python_mypy(ctx, target=None, pdb=False):
    """
    Run mypy.
    For more info: https://mypy.readthedocs.io/en/stable/
    """
    mypy_options = "--cache-dir=/dev/null"

    if pdb:
        mypy_options += " --pdb"

    if target is None:
        target = " --package {{ cookiecutter.python_package_name }}"
    else:
        target += " --follow-imports=silent"

    command = f"dmypy run -- {target} {mypy_options}"

    ctx.run("dmypy --version")
    ctx.run(command=command, pty=True)


@task
def run_python_import_linter(ctx):
    """
    Run import linter.
    For more info: https://import-linter.readthedocs.io/
    """
    with ctx.cd(f"{constants.PROJECT_ROOT}/src"):
        ctx.run(
            "lint-imports --config=../pyproject.toml --verbose --no-cache",
            pty=True,
        )


@task(positional=["path"], iterable=["path"], optional=["path"])
def run_python_fixit_linter_on_paths(ctx, path):
    """
    Run Fixit to lint the provided paths.
    """
    ctx.run(f"fixit lint {' '.join(path)}", pty=True)
