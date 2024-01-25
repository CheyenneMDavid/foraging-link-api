"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage uservfollowers from the admin panel.
"""

from django.contrib import admin
from .models import Follower

admin.site.register(Follower)
