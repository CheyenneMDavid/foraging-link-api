"""
This module defines the URL patterns that are associated with the views in
the posts app.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.urls import path
from posts import views

# URL patterns for post list views
urlpatterns = [
    path("posts/", views.PostList.as_view()),
]
