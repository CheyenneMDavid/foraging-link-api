"""
This module defines the module defines the PlantsInFocus serializer and
related functionalities.

The function to validate images is a direct copy from the Code Institute DRF-API walkthrough project, from the posts app, serializer file.
"""


from rest_framework import serializers
from .models import PlantInFocus


class PlantInFocusSerializer(serializers.ModelSerializer):
    """
    Serializer for PlantInFocus model, transforms PlantInFocus model instances
    to and from JSON format and vice-versa.
    """

    class Meta:
        """
        Meta class for PlantInFocusSerializer.

        States the model to be serialized and the fields that need to be
        included.
        """

        model = PlantInFocus

        # Serializing all fields.
        fields = "__all__"


def validate_image(self, value):
    """
    Validation for the file size and dimensions of the image before it's
    uploaded.  If the filesize or image dimensions are outside the
    allowances, a ValidationError is raised.
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
