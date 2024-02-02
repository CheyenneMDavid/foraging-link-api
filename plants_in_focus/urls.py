"""
This module defines the URL patterns that are associated with the views in
the plants_in_focus app.
"""
from django.urls import path
from .views import (
    PlantInFocusList,
    PlantInFocusCreate,
    PlantInFocusUpdateDelete,
)

# individual url patters for each view in the plants_in_focus app.
urlpatterns = [
    path("plants_in_focus/", PlantInFocusList.as_view()),
    path("plants_in_focus/create/", PlantInFocusCreate.as_view()),
    path(
        "plants_in_focus/update_and_delete/<int:pk>/",
        PlantInFocusUpdateDelete.as_view(),
    ),
]
