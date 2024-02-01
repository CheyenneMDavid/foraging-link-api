"""
This model represents a monthly featured plant with details about its common
name, environment, culinary uses, medicinal uses, folklore, and lookalikes.
"""

from django.db import models


class PlantInFocus(models.Model):
    """
    Represents a monthly featured plant with details about it.
    """

    # Using dropdown predefined month names for consistency from admin panel.
    # Using numbers instead of writing the months twice because it looks
    # cleaner.
    MONTH_CHOICES = [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    ]

    # Chosen from dropdown menu.
    month = models.IntegerField(choices=MONTH_CHOICES, blank=False)
    focus_plant_name = models.CharField(max_length=255, blank=False)
    # Remember to add route!
    focus_plant_image = models.ImageField(
        upload_to="images/",
        default="default_image",
    )
    environment = models.TextField(blank=False)
    culinary_uses = models.TextField(blank=False)
    medicinal_uses = models.TextField(blank=False)
    folklore = models.TextField(blank=True)

    lookalike_plant_name = models.CharField(max_length=255, blank=False)
    # Remember to add route!
    lookalike_plant_image = models.ImageField(
        upload_to="images/",
        default="default_lookalike",
    )

    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.common_name
