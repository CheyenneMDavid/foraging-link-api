"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user post from the admin panel.
"""

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Administration object for Post models.
    Defining the fields for list_display, search fields and the list_filter
    """

    # List of fields that will be displayed in the admin panel.
    list_display = ("title", "owner", "created_at", "updated_at")

    # Search fields for the additional functionality.
    search_fields = ["title", "content"]

    # Fields that are used to filter the searches.
    list_filter = ("created_at", "updated_at", "owner")


# Registering the PostAdmin configuration
admin.site.register(Post, PostAdmin)
