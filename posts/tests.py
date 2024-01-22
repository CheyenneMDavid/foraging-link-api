"""
This module defines the test cases for the Post application in Django.

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostListViewTests(APITestCase):
    """
    Tests for the post list view.

    Verifies functionality of the Post list
    view,
    including the ability to list posts and create new posts based on user
    authentication status.
    """

    def setUp(self):
        """
        Set up method to create a user before each test is run.
        """
        User.objects.create_user(username="adam", password="pass")

    def test_can_list_posts(self):
        """
        Ensure we can list posts.

        The test checks that a user can retrieve a list of posts and verifies
        the response.
        """
        adam = User.objects.get(username="adam")  # Get the created user

        # Creates a post owned by adam
        Post.objects.create(owner=adam, title="a title")
        # Makes a GET request to the posts endpoint
        response = self.client.get("/posts/")
        # Asserts that the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Optional: Print response data for debugging
        print(response.data)
        # Optional: Print the length of response data for debugging
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """
        Ensure a logged-in user can create a post.

        This test verifies that an authenticated user can successfully create
        a post
        and checks the response status and post count in the database.
        """
        self.client.login(username="adam", password="pass")  # Log in the user
        # Makes a post request to create a new post
        response = self.client.post("/posts/", {"title": "a title"})
        # Get the count of Post objects in the database
        count = Post.objects.count()
        # Assert that one Post has been created
        self.assertEqual(count, 1)
        # Assert the response status is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        """
        Ensure a non-authenticated user cannot create a post.

        This test checks that a request to create a post by an unauthenticated
        user
        results in a 403 Forbidden response.
        """
        # Attempt to create a post without logging in
        response = self.client.post("/posts/", {"title": "a title"})
        # Assert the response status is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
