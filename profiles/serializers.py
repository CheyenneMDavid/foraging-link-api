"""
This module defines the Profile serializers and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""


from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model. It includes read-only fields and
    defines the fields that are serialized/deserialized. The 'owner' field is
    read-only and gets the username of the profile owner.
    """

    # Profile owner's username.
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Checks if the user that's making the request is the owner of the
        profile. If they are, it returns a true.  Else, it's a false.
        """
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        """
        Meta class for the ProfileSerializer.
        It specifies the model to be used for serialization (Profile) and
        defines the fields that should be included in the serialized output.
        """

        model = Profile
        # Fields are being explicitly stated to allow the adding of fields to
        # the profile model which I may not wish to have in the serializer.
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "user_bio",
            "image",
            "is_owner",
        ]
