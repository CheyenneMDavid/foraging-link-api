"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user profiles from the admin panel.
"""

from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    Defining the fields in the admin panel. The criteria and filtering of the
    searches.
    """

    # Fields for the admin's list view.
    list_display = ("owner", "created_at", "updated_at")

    # Fields to enable search functionality. Allowing the admins to find
    # profiles according to user names and their bios.
    search_fields = ["owner", "user_bio", "owner__username"]

    # Filter fields to sort by date the profiles were created or updated.
    list_filter = ("created_at", "updated_at")


# Registering the ProfileAdmin configuration.
admin.site.register(Profile, ProfileAdmin)
