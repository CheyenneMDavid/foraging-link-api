"""
This module defines the Profile model and related functionalities.

Much of the code in this file is copied from the django walkthrough projects
with Code Institute.
"""

# Importing necessary Django modules
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing user profiles.
    """

    # Creating a one to one relationship with the user model
    # Using SET_NULL to ensure posts are retained when a user deletes their
    # account, setting the username to innactive user.
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    # Automatically sets the profile creation date and time.
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically updates the timestamp when the profile is changed.
    updated_at = models.DateTimeField(auto_now=True)
    # Both the name and content allow for blank input.
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    # Uses a default image for uploads if none is provided.
    image = models.ImageField(
        upload_to="images/", default="../default_profile_pic_ciw1he.jpg"
    )

    class Meta:
        """
        Meta class for defining model options.
        """

        # Ensures that the newest profiles are shown first.
        ordering = ["-created_at"]

    # User's name as a string.
    def __str__(self):
        return f"{self.owner}'s profile"


# Automatically creates a Profile when a new User is created.
def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a profile when a new User is created.
    """
    # Checks if it's a new User instance.
    if created:
        # Creates a Profile for the new User.
        Profile.objects.create(owner=instance)


# Connects the 'post_save' signal from the User model to the create_profile
# function, ensuring a Profile is created everytime a new User is saved for
# the first time.
post_save.connect(create_profile, sender=User)
