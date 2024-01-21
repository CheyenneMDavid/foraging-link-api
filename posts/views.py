"""
This module defines the Post views and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    """
    View for listing posts and creating new ones.
    It supports GET requests for fetching all of the posts and
    POST requests for creating the new ones.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Handles requests to retrieve lists of posts.
        It fetches them from the database, serializes them and then returns
        the serialized data.
        """

        # Fetching all posts.
        posts = Post.objects.all()
        # Serializes the posts
        serializer = PostSerializer(
            posts,
            many=True,
            context={"request": request},
        )
        # Returns the serialized posts.
        return Response(serializer.data)

    def post(self, request):
        """
        Handles requests to create any new posts.
        Deserializes the data and saves the new Post.
        Returns the serialized data of the new post or errors if the data is
        invalid.
        """

        # Deserialize the incoming data to create new posts.
        serializer = PostSerializer(
            data=request.data,
            context={"request": request},
        )
        # If the post is valid, it saves the new post as belonging to the user
        # that made the post request.
        if serializer.is_valid():
            serializer.save(owner=request.user)
            # Returns serialized data of the new post and a http 201, created
            # status.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the post wasn'nt valid, then a 400 bad request is returned.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
