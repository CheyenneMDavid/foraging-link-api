"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage user course registrations from the admin
panel.
"""

from django.contrib import admin
from .models import CourseRegistration

admin.site.register(CourseRegistration)
