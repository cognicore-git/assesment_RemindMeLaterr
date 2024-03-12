"""
URL configuration for the Remind-me-later project.

This module defines URL patterns for handling API requests related to reminders.
"""

from django.urls import path
from reminders.views import ReminderCreateView

urlpatterns = [
    path('api/reminders/', ReminderCreateView.as_view(), name='reminder-create'),
    # Define URL pattern for creating reminders
    # This pattern routes POST requests to the ReminderCreateView to create new reminder objects
]
