import invoke


def _run_python_tests(
        ctx,
        *paths,
        processes=2,
        create_db=True,
        extra_options=None,
        collect_coverage=False,
):
    """
    Run Python tests for the given paths.
    """
    options = ["--capture=fd"]

    if create_db:
        options.append("--create-db")

    if processes > 1:
        options.append(f"--numprocesses={processes}")

    if collect_coverage:
        options.extend(
            ("--cov=.", "--cov-append", "--cov-context test", "--cov-report=")
        )

    if extra_options:
        options.extend(extra_options)

    # Build command
    cmd = "pytest {options} {paths}".format(options=" ".join(options), paths=" ".join(paths))

    print(f"$ {cmd}")  # noqa: K104

    return ctx.run(cmd, pty=True)


@invoke.task
def run_python_functional_tests(ctx, collect_coverage=False):
    """
    Run functional tests.
    """
    _run_python_tests(
        ctx,
        "tests/functional",
        collect_coverage=collect_coverage,
    )


@invoke.task
def run_python_integration_tests(ctx, collect_coverage=False):
    """
    Run integration tests.
    """
    _run_python_tests(
        ctx,
        "tests/integration",
        collect_coverage=collect_coverage,
    )


@invoke.task
def run_python_unit_tests(ctx, collect_coverage=False):
    """
    Run unit tests.
    """
    _run_python_tests(
        ctx,
        "tests/unit",
        collect_coverage=collect_coverage,
    )
