"""
This module defines the module defines the PlantsInFocus serializer and
related functionalities.
"""


from rest_framework import serializers
from .models import PlantInFocus


class PlantInFocusSerializer(serializers.ModelSerializer):
    """
    Serializer for PlantInFocus model.
    """

    class Meta:
        """
        Meta class to define the model and fields that will be converted from
        JSON formnat and back.
        """

        model = PlantInFocus

        # Serializing all fields.
        fields = "__all__"
