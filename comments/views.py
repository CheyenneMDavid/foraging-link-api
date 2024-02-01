"""
This module defines the Comments view and related functionalities.

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
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    This view inherits from "ListCreateAPIView", a generic view for handling
    lists of objects. The permission class is set to
    "IsAuthenticatedOrReadOnly", allowing both authenticated and
    unauthenticated users to view the list of comments,
    but only authenticated users can create any new ones.
    """

    # Serializer class to convert queryset objects to JSON.
    serializer_class = CommentSerializer
    # Using "IsAuthenticatedOrReadOnly
    # so that comments are read only, unless a user is suthenticated.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Using queryset to list all of the profiles
    queryset = Comment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["post"]

    def perform_create(self, serializer):
        """
        Creates a new comment and associates it with the logged-in user.

        This method is called when creating a new comment and ensures
        that the comment is associated with the user who is currently logged
        in.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Inherits from "RetrieveUpdateDestroyAPIView"
    Retrieves a comment, or update or delete it by id if you own it by using
    the permission "IsOwnerOrReadOnly"
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
