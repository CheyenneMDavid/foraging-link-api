"""
This module defines the Comments model and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

# Importing necessary Django modules
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comments are associated with the User who made the comment and the
    the posts that the comments are on.

    Using SET_NULL to ensure posts are retained when a user deletes
    their account, setting the username to inactive user. This way the
    comments can then be retained on the inactive user post.
    If the post it's self deleted, then comments also delete using CASCADE.
    """

    # Associates comments with the users and handles the user accounts being
    # deleted.
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Comments are deleted if the associated post is deleted due to CASCADE.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Automatic timestamp indicating when the comment was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatic timestamp for the last update of the comment.
    updated_at = models.DateTimeField(auto_now=True)
    # The text content of the comment.
    content = models.TextField()

    class Meta:
        """
        Meta class for specifying model options.
        Ensures that the newest profiles are shown first.
        """

        # Orders comments by creation time, with newest first
        ordering = ["-created_at"]

    def __str__(self):
        """
        Returning the comment as a string so that the comment can be read in
        the admin panel, making it easier to moderate.
        """
        return str(self.content)
