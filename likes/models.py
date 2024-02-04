"""
This module defines the Like model and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

# Importing necessary Django modules
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """

    # Linking Like to the User model.  Enables many like instances to belong
    # to a single user that did the likeing. If a User is deleted, all the
    # likes that are attributed to that user are also deleted because of the
    # use of CASCADE
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Linking Like to the Post model. Each Like is related to one single post.
    # 'related_name' allows accessing all likes of a post (post.likes).
    # If the related Post is deleted, this field is set to null (SET_NULL).
    post = models.ForeignKey(
        Post,
        related_name="likes",
        on_delete=models.SET_NULL,
        null=True,
    )

    # Linking Like to the Comment model. Each Like is related to one single
    # comment.
    # 'related_name' allows accessing all likes of a comment (post.likes).
    # If the related Comment is deleted, this field is set to null (SET_NULL).
    comment = models.ForeignKey(
        Comment,
        related_name="likes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # Time stamp of when the like instance was created.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Customizing the default behaviour so that newest appear first.
        Unique to ensure against duplicating likes.
        """

        ordering = ["-created_at"]

        # making two separate fields of unique together fields.  One for the
        # posts and one for comments.
        unique_together = [("owner", "post"), ("owner", "comment")]

    def __str__(self):
        """
        Depending on whether it's a post or a comment that's liked,
        """
        if self.post:
            # If the condition is that its a post that was liked, then what is
            # returned is the owner of the like and posts id.
            return f"{self.owner} likes post {self.post.id}"

        # If it's a comment that was liked, then what is
        # returned is the owner of the like and the comment's id.
        return f"{self.owner} likes comment {self.comment.id}"
