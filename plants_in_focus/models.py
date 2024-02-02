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
    month = models.IntegerField(choices=MONTH_CHOICES)
    featured_item = models.CharField(max_length=255)
    # Remember to add route!
    featured_item_image = models.ImageField(
        upload_to="images/",
        default="default_image",
    )
    environment = models.TextField()
    culinary_uses = models.TextField()
    medicinal_uses = models.TextField()
    folklore = models.TextField()

    lookalike_item = models.CharField(max_length=255, blank=True)
    # Remember to add route!
    lookalike_item_image = models.ImageField(
        upload_to="images/",
        blank=True,
    )

    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.featured_item
