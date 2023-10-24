import sys

import invoke

from tasks import constants


@invoke.task
def build_docs(ctx):
    """
    Build documentations.
    """
    # Run mkdocs to build HTML files
    with ctx.cd(f"{constants.PROJECT_ROOT}/src/docs"):
        cmd = "poetry run mkdocs build"
        ctx.run(cmd, pty=True)


@invoke.task
def serve_docs(ctx):
    """
    Live-reloading documentations.
    """
    # Serve mkdocs to build HTML files
    with ctx.cd(f"{constants.PROJECT_ROOT}/src/docs"):
        cmd = "poetry run mkdocs serve"
        ctx.run(cmd, pty=True)

    sys.exit(build_docs(ctx))
