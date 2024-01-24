"""
This module defines the URL patterns that are associated with the
views in the Likes app.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

# url patterns for likes lists
from django.urls import path
from likes import views

urlpatterns = [
    path("likes/", views.LikeList.as_view()),
]
