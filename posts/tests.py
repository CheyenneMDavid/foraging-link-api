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


class PostDetailViewTests(APITestCase):
    """
    Tests for post detail view
    """

    def setUp(self):
        """
        Creates users and posts before each test is run.
        """

        # Creates users, adam and brian.
        adam = User.objects.create_user(username="adam", password="pass")
        brian = User.objects.create_user(username="brian", password="pass")

        # Creates posts for each user
        Post.objects.create(
            owner=adam,
            title="a title",
            content="adams content",
        )
        Post.objects.create(
            owner=brian, title="another title", content="brians content"
        )

    def test_can_retrieve_post_using_valid_id(self):
        """
        Tests retrieving the posts using a valid ID, ensuring that the correct
        post is retrieved and the status code is a http200, OK.
        """
        # Attempt to retrieve the first post
        response = self.client.get("/posts/1/")
        # Check if the title matches
        self.assertEqual(response.data["title"], "a title")
        # Confirm the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        """
        Test retrieving a post using an invalid ID.
        Ensures that a 404 Not Found response is returned for an invalid post
        ID.
        """
        # Attempt to retrieve a non-existent post
        response = self.client.get("/posts/999/")
        # Confirm the status code is 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """
        Tests that the user can update their own posts and confirms that the
        post title is updated and the status is a http200, OK.
        """
        # Log in as Adam
        self.client.login(username="adam", password="pass")
        # Adam updates his own posts
        response = self.client.put("/posts/1/", {"title": "a new title"})
        # Gets an updates post back.
        post = Post.objects.filter(pk=1).first()
        # Checks if the title is also updated
        self.assertEqual(post.title, "a new title")
        # Confirms that the status is a http200, ok.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        """
        Test that one user can't update another's post.
        Verifies that a 403 Forbidden response is returned when attempting to
        update another user's post.
        """

        # Logs in as adam.
        self.client.login(username="adam", password="pass")
        # Adam tries to update brian's post.
        response = self.client.put("/posts/2/", {"title": "a new title"})
        # Confirms that the status code is a http 403, forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
