from django.urls import path

from . import views

urlpatterns = [
    path("", views.Account.as_view(), name="index"),
]
