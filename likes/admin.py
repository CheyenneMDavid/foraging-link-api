"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage likes from the admin panel.
"""
from django.contrib import admin
from .models import Like


class LikeAdmin(admin.ModelAdmin):
    """
    Administration for Like models, defining the list view, search capability, and filters.
    """

    # Fields to display in the admin interface
    list_display = ("post", "owner", "created_at")

    # Fields on which search functionality is enabled
    search_fields = ["post__title", "owner__username"]

    # Filters to apply in the admin list view
    list_filter = ("created_at",)


# Registering the Like model with LikeAdmin configuration
admin.site.register(Like, LikeAdmin)
