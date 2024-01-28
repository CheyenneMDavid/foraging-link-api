"""
The code in this view is copied from the drf-api walkthrough
project with Code Institute.

The view's purpose is to profide a welcome message and ensure the user is able 
to logout and does this by setting the cookies to empty strings
"""


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    """
    Returns with a welcome message "Welcome to 'The Foraging Link API' "
    """

    return Response({"message": "Welcome to 'The Foraging Link API'"})


@api_view(["POST"])
def logout_route(request):
    """
    Logout route view.
    Clearing the JWT tokens stored in cookies.
    """

    response = Response()

    # Clear JWT Auth Cookie
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        # Setting value to an empty string.
        value="",
        httponly=True,  # Restricts the access to the cookie from JavaScript
        # ensure invalid by setting expiry to an old date.
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )

    # Clear JWT Auth Refresh Cookie using the same parameters
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )

    # Return the response with cleared cookies
    return response
