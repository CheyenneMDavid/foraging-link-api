"""
This module defines the URL patterns that are associated with the
views in the profiles app.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.urls import path
from profiles import views

# URL patterns for profiles lists and detail views
urlpatterns = [
    path("profiles/", views.ProfileList.as_view()),
    path("profiles/<int:pk>/", views.ProfileDetail.as_view()),
]
