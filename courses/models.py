"""
Purpose of the Course model is to store information about courses offered
within the main application.
"""

from django.db import models


class Course(models.Model):
    """
    model representing the content/details of a course
    """

    # Using dropdown predefined season names for consistency from admin panel.
    SEASON_CHOICES = [
        ("", "Select Season"),
        ("Spring", "Spring"),
        ("Summer", "Summer"),
        ("Autumn", "Autumn"),
    ]

    # Using dropdown predefined course durations.
    DURATION_CHOICES = [
        ("", "Select Duration"),
        ("Half Day", "Half Day"),
        ("Full Day", "Full Day"),
    ]

    # Always will be presented with three seasons.
    season = models.CharField(
        max_length=25, choices=SEASON_CHOICES, default="", blank=False
    )

    # Course title, independent, different each time.
    title = models.CharField(max_length=255)

    # Only the Date field required.
    date = models.DateField()

    # Large undefined text field
    description = models.TextField()

    location = models.CharField(max_length=255)

    # Preset and fixed number because this will never change.
    max_capacity = models.PositiveIntegerField(default=10, editable=False)

    # Always will be presented with either a half-day or a full-day.
    duration = models.CharField(
        max_length=25,
        choices=DURATION_CHOICES,
        default="",
        blank=False,
    )

    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.title
