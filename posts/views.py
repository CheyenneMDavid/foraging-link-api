"""
This module defines the Post view and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough
project with Code Institute and the refactoring of this view is
sepcifically based on the "CommentList and CommentDetail generic views"
lesson here:
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/10d957d204794dbf9a4410792a58f8eb/
"""

# Import necessary Django and DRF modules
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from foraging_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    This view provides the list of all posts.

    Inherits from ListCreateAPIView, a generic view for handling lists,
    retrieving and creation. The permission class is
    "IsAuthenticatedOrReadOnly", so posts can be read by anyone, but only
    created by an authenticated user.
    """

    # Serializer class to convert queryset objects to JSON.
    serializer_class = PostSerializer
    # Using "IsAuthenticatedOrReadOnly" so that lists of posts are read only
    # unless the user is signed in.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Using queryset to list all of the posts.
    queryset = Post.objects.annotate(
        likes_count=Count("likes", distinct=True),
        comments_count=Count("comment", distinct=True),
    ).order_by("-created_at")

    # Configuration of "filters" and "search"
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    # Defining the fields to filter the posts.
    filterset_fields = [
        "owner__followed__owner__profile",
        "likes__owner__profile",
        "owner__profile",
    ]

    # Definig the fields that will be used for searching the posts.
    search_fields = [
        "owner__username",
        "title",
    ]

    # Defining the order of the posts.
    ordering_fields = [
        "likes_count",
        "comments_count",
        "likes__created_at",
    ]

    def perform_create(self, serializer):
        """
        The "perform_create" method has been customized in order to
        override it's default behaviour. The addidtional customization reslts
        in the post being associated with the the owner that is making the
        reqest.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Inheriting from "RetrieveUpdateDestroyAPIView", providing  get, put, patch
    and delete method handlers.
    """

    # Queryset for fetching Post objects
    queryset = Post.objects.annotate(
        likes_count=Count("likes", distinct=True),
        comments_count=Count("comment", distinct=True),
    ).order_by("-created_at")
    # Serializer for Post objects
    serializer_class = PostSerializer
    # Permission classes for controlling the ability to make changes to the
    # post.
    permission_classes = [IsOwnerOrReadOnly]
