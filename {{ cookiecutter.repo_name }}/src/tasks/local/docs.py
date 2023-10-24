import invoke
import os


@invoke.task
def build_docs(ctx):
    """
    Build sphinx documentations.
    """
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "{{ cookiecutter.python_package_name }}.settings.configuration.localhost"
    )  # noqa: K118

    ctx.run("rm -rf docs/_build/")

    # Run Sphinx to build HTML files
    cmd = (
        "sphinx-build -b html -a -E -W -T -v "
        "-c docs/ "
        "docs/ "
        "docs/_build/"
    )
    ctx.run(cmd, pty=True, hide=True)
