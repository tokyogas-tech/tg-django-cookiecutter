#!/bin/sh

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

cd /var
git clone --depth=1 https://github.com/pyenv/pyenv.git $HOME/.pyenv
pyenv install {{ cookiecutter.python_long_version }}
pyenv global {{ cookiecutter.python_long_version }}
pyenv rehash

cd /var/{{ cookiecutter.repo_name }}
pip install virtualenv
virtualenv -p $(which python3) .venv
. .venv/bin/activate
pip install poetry
poetry install
poetry export --without-hashes --format=requirements.txt > requirements.txt
poetry export --without-hashes --with dev --format=requirements.txt > requirements.dev.txt
cd src
python3 manage.py makemigrations --settings={{ cookiecutter.python_package_name }}.settings.configuration.localhost
python3 manage.py migrate --settings={{ cookiecutter.python_package_name }}.settings.configuration.localhost
python3 manage.py createsuperuser --username=admin --email=info@test.com --noinput --settings={{ cookiecutter.python_package_name }}.settings.configuration.localhost
