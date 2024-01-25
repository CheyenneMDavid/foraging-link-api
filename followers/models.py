"""
This module defines the Follower model and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

# Importing necessary Django modules

from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Defining the Follower model, representing the relationship between users
    as followers of one another.

    "CASCADE" upon delete is used for both the "owner" who is the user that is
    following and also "followed" who is the user that us being followed. This
    ensures that records are deleted every which way, leaving things clean,
    unlike the likes and comments models where deleted users are changed to
    inactive, there by retaining information such as posts, comments on posts
    and the liking of posts.
    """

    owner = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE,
    )
    followed = models.ForeignKey(
        User,
        related_name="followed",
        on_delete=models.CASCADE,
    )
    # Automatically sets the date and time when follow record is made
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        """
        Overiding the default behaviour by listing followers, newest first.
        Using "unique_together" so Users can't  double up on following.
        """

        ordering = ["-created_at"]
        unique_together = [
            "owner",
            "followed",
        ]

    def __str__(self):
        return f"{self.owner} {self.followed}"
