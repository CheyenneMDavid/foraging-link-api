"""
Purpose of the Course model is to store information about courses offered
within the main application
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
    max_capacity = models.PositiveIntegerField()
    duration = models.CharField(max_length=20, default="10hrs", editable=False)

    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.title
