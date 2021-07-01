from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    # order is important, integers are also considered as string if we mention that first
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
    # month is a variable
]
