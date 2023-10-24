#!/bin/bash
# This script is called on AWS Batch Job
sh -eux -c '
poetry run python src/manage.py makemigrations --no-input &&
poetry run python src/manage.py migrate --no-input &&
poetry run python src/manage.py collectstatic --no-input &&
poetry run python src/manage.py update_group_perms &&
poetry run python src/manage.py finduser --username admin ||
poetry run python src/manage.py createsuperuser --username=admin --email=info@example.com --no-input
'
