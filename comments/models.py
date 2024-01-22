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
    Comment model, related to User and Post

    Comments are related to the User who is commenting and the post that
    the comment's on.
    """

    # ForeignKey relationship to the User model. Each comment is owned by a
    # user.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey relationship to the Post model. Each comment is related to a
    # post.
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
