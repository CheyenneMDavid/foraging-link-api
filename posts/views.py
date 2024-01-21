"""
This module defines the Post views and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from foraging_api.permissions import IsOwnerOrReadOnly
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
        # If the post was'nt valid, then a 400 bad request is returned.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Gets, Updates and Deletes single posts.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get_object(self, pk):
        """
        Gets a post using it's primary key (pk) and
        raises a 404 error if it's
        not found.
        """
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Handles a get request for a single post and returns it as serialized data.
        """
        post = self.get_object(pk)
        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Handles a put request for th updating of a single post.
        If the the data's valid, it updates the post and returns it.
        """
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Handles the delete request for a single post. Deleting and returning a
        http204 after successful deleting.
        """
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
