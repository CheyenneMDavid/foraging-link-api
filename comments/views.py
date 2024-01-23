"""
This module defines the Comments view and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from rest_framework import generics, permissions
from foraging_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """
        Creates a new comment and associate it with the logged-in user.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves a comment, or update or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
