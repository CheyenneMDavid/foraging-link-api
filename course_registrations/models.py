"""
Purpose of the CourseRegistrations model is to store information about courses
offered
within the main application.
"""
from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
]


class CourseRegistration(models.Model):
    """
    This model represents a user's registration for a course and hold relevent
    data accordingly.  The "Status" field defaults to "Pending". This ensures
    courses aren't over subscribed.  It can also then be controlled with
    additinal back end logic when added.
    """

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now=True)
    # Defaults to "Pending", can be changed from the admin panel or by backend
    # logic when implemented
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending",
    )
    dietary_restrictions = models.TextField(blank=True, null=True)
    is_driver = models.BooleanField(default=False)
    # In Case of Emergency name & number
    ice_name = models.CharField(max_length=255)
    ice_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name.username
