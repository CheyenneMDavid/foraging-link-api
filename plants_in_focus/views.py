"""
This module defines the PlantsInFocus view and related functionalities.

Much of the code in this file is copied from the drf-api walkthrough
project with Code Institute and the refactoring of this view is
sepcifically based on the "CommentList and CommentDetail generic views"
lesson here:
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/10d957d204794dbf9a4410792a58f8eb/
"""

from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import PlantInFocus
from .serializers import PlantInFocusSerializer


class PlantInFocusList(generics.ListAPIView):
    """
    This view inherits from "ListAPIView" and ONLY retrives and then presents
    the instances in a read-only format.  Using the List APIView like this
    allows it to have the permission class of "AllowAny", enabling a user to
    read the content whether they are authenticated or not.
    """

    # Using "all()" to fetch all instances
    queryset = PlantInFocus.objects.all()
    serializer_class = PlantInFocusSerializer
    # Permission class that make it available to read by anyone.
    permission_classes = [AllowAny]

    # Configuration of "filters" and "search"
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    # Definig the fields that will be used for searching the posts.
    search_fields = [
        "month",
        "environment",
        "culinary_uses",
        "folklore",
    ]


class PlantInFocusCreate(generics.CreateAPIView):
    """
    This inherits from "CreateAPIView" and as such is assigned the permission
    class of "IsAdmin" so that nobody else can make any changes to the
    instances.
    """

    queryset = PlantInFocus.objects.all()
    serializer_class = PlantInFocusSerializer
    # Permission to ensure a record can only be Read, Updated or Deleted by
    # someone who is an Admin.
    permission_classes = [IsAdminUser]


class PlantInFocusUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    This inherits from "RetrieveUpdateDestroyAPIView" and as such is assigned
    the permission class of "IsAdmin" so that nobody else can make any changes
    to the PlantInFocus instances but it allows read-only access to the
    individual instances.
    """

    queryset = PlantInFocus.objects.all()
    serializer_class = PlantInFocusSerializer
    # Permission to ensure a record can only be Read, Updated or Deleted by
    # someone who is an Admin.
    permission_classes = [IsAdminUser]
