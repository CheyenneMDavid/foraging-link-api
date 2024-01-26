"""
This module defines the Profile serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""


from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model. It includes read-only fields and
    defines the fields that are serialized/deserialized. The 'owner' field is
    read-only and gets the username of the profile owner.
    """

    # Profile owner's username.
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Checks if the user making the request is the owner of the
        profile. Returns True if they are, otherwise False.
        """
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Gets the ID of the user who's following the profile.

        If the a user isn't authenticated of if there's no followers, then
        "None" is returned.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner,
            ).first()
            # print(following)
            return following.id if following else None
        return None

    class Meta:
        """
        Meta class for the ProfileSerializer.
        It specifies the model to be used for serialization (Profile) and
        defines the fields that should be included in the serialized output.
        """

        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "user_bio",
            "image",
            "is_owner",
            "following_id",
        ]
