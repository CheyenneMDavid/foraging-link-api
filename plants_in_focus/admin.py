"""
Admin configuration to register the model with the Django admin interface,
allowing administrators to manage publishing the monthly plants from the admin
panel.
"""

from django.contrib import admin
from .models import PlantInFocus

admin.site.register(PlantInFocus)
