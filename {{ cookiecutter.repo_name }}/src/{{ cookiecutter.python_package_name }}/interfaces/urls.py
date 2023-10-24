from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.defaults import server_error, page_not_found
from django.views.generic import RedirectView


FAVICON_PATH = getattr(settings, "FAVICON_PATH")

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=FAVICON_PATH, permanent=False), name="favicon"),
    re_path("^", include("{{ cookiecutter.python_package_name }}.interfaces.authentication.urls"), name="authentication"),
    re_path(r"^accounts/", include("{{ cookiecutter.python_package_name }}.interfaces.accounts.urls"), name="accounts"),
    re_path(r"^django-admin/", admin.site.urls),
    re_path(r"^docs/", include('django.contrib.admindocs.urls')),
]

if settings.DEBUG:
    try:
        import debug_toolbar  # type: ignore
        urlpatterns += [
            path("__debug__/", include(debug_toolbar.urls)),
            path("500/", server_error),
            path("404/", page_not_found),
        ]
    except ImportError:
        pass