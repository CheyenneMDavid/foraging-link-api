"""
This module defines the Post serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model handling the conversion of comments,
    to and from JSON format.
    """

    # Read-only field to get the username of the comment owner.
    owner = serializers.ReadOnlyField(source="owner.username")

    # Method field determines if the current request user is the owner of the
    # comment.
    is_owner = serializers.SerializerMethodField()

    # Read-only fields getting profile-related information of the comment
    # owner.
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")

    def get_is_owner(self, obj):
        """
        Returns "True" if the requesting user is the owner of the
        post. If they're not, it returns a "False"
        """
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        """
        Specifies the model to be used and says which fields will be
        included
        """

        model = Comment
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "post",
            "created_at",
            "updated_at",
            "content",
        ]
