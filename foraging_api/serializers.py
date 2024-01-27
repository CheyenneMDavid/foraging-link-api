"""
This module defines the main applications serializers and related
functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Inherits from "UserDetailsSerializer" and extends it's functionality by
    adding aditional fields to be serialized.
    """

    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_image = serializers.ReadOnlyField(source="profile.image.url")

    class Meta(UserDetailsSerializer.Meta):
        """
        The additional fields that will be serialized.
        """

        fields = UserDetailsSerializer.Meta.fields + (
            "profile_id",
            "profile_image",
        )
