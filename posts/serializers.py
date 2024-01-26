"""
This module defines the Post serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from rest_framework import serializers
from posts.models import Post
from likes.models import Like


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
    profile_id = serializers.ReadOnlyField(
        source="owner.profile.id",
    )
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.image.url",
    )
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Validation for the file size and dimensions of the image before it's
        uploaded.  If the filesize or image dimensions are outside the
        allowances, a ValidationError is rasied.
        """

        # Allowances for image file size and dimensions.
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image size larger than 2MB!",
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height larger than 4096px!",
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width larger than 4096px!",
            )
        return value

    def get_is_owner(self, obj):
        """
        Returns "True" if the requesting user is the owner of the
        post. If they're not, it returns a "False"
        """
        request = self.context["request"]

        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Gets the  of the user's like for a particular post. Or None if it's not liked.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

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
            "like_id",
        ]
