"""
This module defines the Post model and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    # Creating a many to one relationship with the user model
    # Using SET_NULL to ensure posts are retained when a user
    # deletes their account, setting the username to inactive user.
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Automatically set the field to now when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically set the field to now every time the object is saved.
    updated_at = models.DateTimeField(auto_now=True)
    # Title of the post, max length 255 characters.
    title = models.CharField(max_length=255)
    # Content of the post. Optional (blank=True).
    content = models.TextField(blank=True)
    # Image field with a default image.
    image = models.ImageField(
        upload_to="images/", default="../default_post_pic", blank=True
    )

    class Meta:
        """
        Meta class for specifying model options.
        Ensures that the newest profiles are shown first.
        """

        ordering = ["-created_at"]

    # String representation of the Post model.
    def __str__(self):
        return f"{self.id} {self.title}"
