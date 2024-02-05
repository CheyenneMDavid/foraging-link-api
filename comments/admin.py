"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user comments from the admin panel.
"""

from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    """
    Administration object forr the Comment models with settings for the list
    display, search with filters.
    """

    # Fields that will be displayed in the admin panel.
    list_display = ("post", "owner", "created_at", "updated_at")

    # Enables the search functionality for fields
    search_fields = ["content", "owner__username"]

    # Field that are used to filter the searches.the list view
    list_filter = ("created_at", "updated_at")


# Registering the CommentAdmin.
admin.site.register(Comment, CommentAdmin)
