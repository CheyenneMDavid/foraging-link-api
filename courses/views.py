"""
This module defines the Course view and related functionalities.

The content of the courses needs to be available to read by users whether they
are authenticated or not.  But only changed in any way by Admins.  To achieve
this, I've separated the functions accordingly.
The ListAPIView allowing it to be read by anyone, whilst both the other two
are accessible by Admins only.
I could have had the same effect could have been achieved with less lines of
code by using "ModelViewSet" because it inherits from "GenericAPIView", but I
felt that having the views separated in this manner allowed them to be more
descriptive at a glance of there individual names.
"""

from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


class CourseList(generics.ListAPIView):
    """
    This view inherits from "ListAPIView" and ONLY retrives and then presents
    them in a read-only format.  Using the List APIView like this allows it to
    have the permission class of "AllowAny", enabling a user to read the
    content whether they are authenticated or not.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # Permission class that make it available to read by anyone.
    permission_classes = [AllowAny]


class CourseCreate(generics.CreateAPIView):
    """
    This inherits from "CreateAPIView" and as such is assigned the permission
    class of "IsAdmin" so that nobody else can make any changes to them.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # Permission to ensure it can only be created by someone who is authorised.
    permission_classes = [IsAdminUser]


class CourseUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    This inherits from "RetrieveUpdateDestroyAPIView" and as such is assigned
    the permission class of "IsAdmin" so that nobody else can make any changes
    to the course but it allows read-only access to the detail of a course.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # Permission to ensure it can only be created by someone who is authorised.
    permission_classes = [IsAdminUser]
