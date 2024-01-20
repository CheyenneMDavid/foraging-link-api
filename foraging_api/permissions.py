"""
This module defines the permissions for the API

Much of the code in this file is copied from the drf-api walkthrough projects
with Code Institute.
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allow owners of an object to edit.
    All other requests get permissions to read.

    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to everyone.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only the owners are allowed "write" permissions
        return obj.owner == request.user
