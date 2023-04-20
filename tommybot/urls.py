# urls.py

from django.urls import path
from .views import tommybot

urlpatterns = [
    path('webhook/', tommybot.as_view()),
]
