"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user profiles from the admin panel.
"""

from django.contrib import admin
from .models import Course

admin.site.register(Course)
