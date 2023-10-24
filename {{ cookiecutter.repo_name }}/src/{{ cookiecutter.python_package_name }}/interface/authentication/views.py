from typing import Any

from django import http
from django.http import request, response
from django.views import generic


class Login(generic.TemplateView):
    def dispatch(self, request: request.HttpRequest, *args: Any, **kwargs: Any) -> response.HttpResponseBase:
        """ログイン画面

        詳細説明

        Arguments:
            request request.HttpRequest: HttpRequestオブジェクト
            args list:
            kwargs dict:

        Returns:
            response.HttpResponseBase: HttpResponseBaseオブジェクト
        """
        return http.HttpResponse("Hello from {{ cookiecutter.service_name }}")
