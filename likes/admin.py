"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user likes from the admin panel.
"""

from django.contrib import admin
from .models import Profile

admin.site.register(Likes)
