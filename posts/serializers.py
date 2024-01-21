"""
This module defines the Post serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model handling the conversion of Posts,
    to and from JSON format.
    """

    # Read only field that fetches the name of the post owner.
    owner = serializers.ReadOnlyField(source="owner.username")
    # Method field, determining if the user that's making the request
    # is the owner of the post.
    is_owner = serializers.SerializerMethodField()
    # Read only fields that get the profile information of the post
    # owner.
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")

    def get_is_owner(self, obj):
        """
        Returns "True" if the requesting user is the owner of the
        post. If they're not, it retuirns a "False"
        """
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        """
        Specifies the model to be used and says which fields will be
        included
        """

        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
        ]
