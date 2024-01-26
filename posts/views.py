"""
This module defines the Post view and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough
project with Code Institute and the refactoring of this view is
sepcifically based on the "CommentList and CommentDetail generic views"
lesson here:
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/10d957d204794dbf9a4410792a58f8eb/

Note:
    The view relies on Django's built-in 404 handling for object not found
    errors.
"""

# Import necessary Django and DRF modules
from django.db.models import Count
from rest_framework import generics, permissions
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

    # Using queryset to list all of the posts.
    queryset = Post.objects.annotate(
        comments_count=Count("owner__comment", distinct=True),
        likes_count=Count("owner__like", distinct=True),
    )
    # Serializer class to convert queryset objects to JSON.
    serializer_class = PostSerializer
    # Using "IsAuthenticatedOrReadOnly" so that lists of posts are read only
    # unless the user is signed in.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
