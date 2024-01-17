"""
This module defines the Profile views and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

# Importing necessary Django modules
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    """
    This view only supports GET requests to retrieve all of the profiles. The
    actual profile creation is handled by Django signals, not this.
    """

    def get(self, request):
        """
        Handles GET requests to retrieve all profiles.
        """

        # Gets all the profiles.
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        # Returns JSON serialised data.
        return Response(serializer.data)
