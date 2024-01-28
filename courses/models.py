"""
Purpose of the Course model is to store 
information about courses offered within the main application
"""

from django.db import models


class Course(models.Model):
    """
    model representing the content/details of a course
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    max_capacity = models.PositiveIntegerField()
    season = models.CharField(max_length=100)

    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.title
