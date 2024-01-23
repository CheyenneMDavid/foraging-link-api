"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user comments from the admin panel.
"""

from django.contrib import admin
from .models import Comment

admin.site.register(Comment)