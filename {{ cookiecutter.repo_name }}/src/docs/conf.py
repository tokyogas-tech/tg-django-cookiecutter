import datetime
import os
import sys

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{ cookiecutter.python_package_name }}.settings.configuration.localhost"
)
sys.path.insert(0, os.path.abspath("../"))

extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
    "sphinxcontrib.mermaid",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "sphinxcontrib_django2",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

project = "{{ cookiecutter.service_name }}"
copyright = f"{datetime.date.today().year}, {{ cookiecutter.service_name }}"
author = "{{ cookiecutter.service_name }}"

html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": -1,
    "style_external_links": True,
    "style_nav_header_background": "#180848",
}
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

myst_heading_anchors = 6
myst_enable_extensions = [
    "smartquotes",
    "deflist",
    "fieldlist",
]
