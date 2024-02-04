"""
This module defines the Profiles view and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough
project with Code Institute and the refactoring of this view is
sepcifically based on the "CommentList and CommentDetail generic views"
lesson here:
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/10d957d204794dbf9a4410792a58f8eb/
"""
# Importing necessary modules
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from foraging_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Inherits from "ListCreateApi" which allows it to read and write

    "IsAuthenticatedOrReadOnly" allows all users to see "likes" but only
    authenticated users are able to "like".
    """

    # Queryset to fetch all the Like.
    queryset = Like.objects.all()
    # Serializer class to handle the serialization of Likes
    serializer_class = LikeSerializer
    # Set to "IsAuthenticatedOrReadOnly"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["post", "owner"]

    def perform_create(self, serializer):
        """
        The "perform_create" method has been customized in order to
        override its default behaviour. The adidtional customization results
        in the likes being associated with the the owner that is making the
        request to like.
        """

        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Inherits from RetrieveDestroyAPIView which gives it method handlers to
    retrieve and destroy the likes.

     By using the permission class of "IsOwnerOrReadyOnly" ensures that only
     the owner of the like can delete it.
    """

    # Permissions to restrict deletion to the owner of the like
    permission_classes = [IsOwnerOrReadOnly]
    # Serializer class for handling Likes
    serializer_class = LikeSerializer
    # Queryset for fetching all likes.
    queryset = Like.objects.all()
