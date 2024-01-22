"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user post from the admin panel.
"""

from django.contrib import admin
from .models import Post

admin.site.register(Post)
