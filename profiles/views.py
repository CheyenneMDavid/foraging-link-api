"""
This module defines the Profiles view and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough
project with Code Institute and the refactoring of this view is
sepcifically based on the "CommentList and CommentDetail generic views"
lesson here:
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/10d957d204794dbf9a4410792a58f8eb/
"""

# Importing necessary modules
from django.http import Http404
from rest_framework import generics, permissions
from foraging_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    This view provides the list of all profiles.

    Inherits from ListAPIView, a generic view for handling
    lists of objects. The permission class is "IsAuthenticated", so only
    authenticated users can read the list of profiles.
    """

    # Using queryset to list all of the profiles
    queryset = Profile.objects.all()
    # Serializer class to convert queryset objects to JSON.
    serializer_class = ProfileSerializer
    # Using "IsAuthenticated" in order to access a list of profiles
    # so that only authenticated users are able to read one another's profiles.
    permission_classes = [permissions.IsAuthenticated]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    This view handles individual profile objects, supporting retrieval
    and update operations.

    Inherits from RetrieveUpdateAPIView, a generic view for handling
    individual objects. Its configured to allow only the owner of a
    profile to modify it by using "IsOwnerOrReadOnly" as the permission
    class.
    """

    # Queryset defines the scope; in this case, all Profile instances.
    queryset = Profile.objects.all()
    # Serializer class to handle serialization and deserialization.
    serializer_class = ProfileSerializer
    # Custom permission to ensure only owners can modify their profile.
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        """
        The "get_object" method has been customized in order to
        override it's default behaviour when fetching a specific
        profile.  The default is that the record be returned using
        only it's primary key.  But because of the aditional
        permission checks being excercised here, the method needs to
        be called in a more specific manner.

        If the profile doesn't exist, then a Http404 is raised.
        """
        pk = self.kwargs.get("pk")
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
