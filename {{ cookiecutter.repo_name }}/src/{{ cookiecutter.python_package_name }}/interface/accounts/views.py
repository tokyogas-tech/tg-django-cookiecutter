import random
import string
from typing import Any

from django import http
from django.http import request, response
from django.views import generic

from . import tasks


class Account(generic.TemplateView):
    def _create_email(self, size: int = 6, chars: str = string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size)) + "@test.com"

    def dispatch(self, request: request.HttpRequest, *args: Any, **kwargs: Any) -> response.HttpResponseBase:
        """アカウント画面

        詳細説明

        Arguments:
            request request.HttpRequest: HttpRequestオブジェクト
            args list:
            kwargs dict:

        Returns:
            response.HttpResponseBase: HttpResponseBaseオブジェクト
        """
        for _ in range(0, 10):
            tasks.test_tasks.apply_async(kwargs={"email": self._create_email()})
        return http.HttpResponse("Check <a href=\"http://0.0.0.0:1080/\" target=\"_blank\">http://0.0.0.0:1080/</a>")
