"""
This module defines the Profile views and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

# Importing necessary Django modules
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from foraging_api.permissions import IsOwnerOrReadOnly
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
        serializer = ProfileSerializer(
            profiles, many=True, context={"request": request}
        )
        # Returns JSON serialised data.
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    This only supports retrieving a single profile detail and updating it.
    """

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Retrieves a profile using it's pk and raises 404 erros if
        one doesn't exist.
        """
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404  # Raise a 404 error if the profile does not exist.

    def get(self, request, pk):
        """
        Handles GET request for a single profile.
        Retrieves a profile by its id and returns the serialized profile data.
        """
        # Retrieves the profile.
        profile = self.get_object(pk)
        # Serialize the profile.
        serializer = ProfileSerializer(profile, context={"request": request})
        # Returns the serialized data..
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Handles PUT request for a single profile.
        Updates a profile and returns it with new data.
        """
        # Retrieve the profile
        profile = self.get_object(pk)
        # Serialize the profile with the new data
        serializer = ProfileSerializer(
            profile, data=request.data, context={"request": request}
        )
        # Checks if the data is valid.
        if serializer.is_valid():
            # Saves the updated profile data.
            serializer.save()
            # Returns the updated profile data.
            return Response(serializer.data)
            # Return errors if the data is invalid.
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # Return errors if the data is invalid.
