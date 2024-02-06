"""
This module defines the Profile model and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
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
    # Using SET_NULL to ensure posts are retained when a user deletes
    # their account, setting the username to inactive user.
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    # Automatically sets the profile creation date and time.
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically updates the timestamp when the profile is changed.
    updated_at = models.DateTimeField(auto_now=True)

    # Originally I had a name field as part of this model, because I felt that
    # it completed what a profile model should contain.  However, when I added
    # the additional functionality of the profile model to the django panel, I
    # realised that it was redundant because of django's built in user model,
    # so I've removed it.

    # Optional information about self, by user.
    user_bio = models.TextField(blank=True)
    # Uses a default image for uploads if none is provided.
    image = models.ImageField(
        upload_to="images/", default="../default_profile_pic_ciw1he.jpg"
    )

    class Meta:
        """
        Meta class for specifying model options.
        Ensures that the newest profiles are shown first.
        """

        ordering = ["-created_at"]

    # User's name as a string.
    def __str__(self):
        return f"{self.owner}'s profile"


# Automatically creates a Profile when a new User is created.
# Using an underscore to stop the linting messages, and more importantly,
# explain to a reader that these are unused variables as per the "Rationale"
# and advice found here:
# https://peps.python.org/pep-0640/#:~:text=with%20each%20other.-,
# Rationale,is%20not%20a%20special%20variable.
def create_profile(_sender, instance, created, **_kwargs):
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
