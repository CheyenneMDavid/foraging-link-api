"""
This module defines the URL patterns that are associated with the views in
the posts app.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.urls import path
from courses import views

# URL patterns for post list views
urlpatterns = [
    path("courses/", views.CourseList.as_view()),
    path("courses/create/", views.CourseCreate.as_view()),
    path("courses/<int:pk>/", views.CourseUpdateDelete.as_view()),
]
