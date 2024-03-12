"""
Configuration for the 'reminders' app.

This module defines the AppConfig class for the 
'reminders' app, providing configuration options 
such as the default auto field for models and the name of the app.

Classes:
    RemindersConfig: AppConfig class for the 'reminders' app.
"""

from django.apps import AppConfig


class RemindersConfig(AppConfig):
    """
    AppConfig class for the 'reminders' app.

    This AppConfig class defines configuration options 
    for the 'reminders' app.
    It specifies the default auto field to use for models 
    and sets the name of the app.

    Attributes:
        default_auto_field (str): The name of the default 
        auto field to use for models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'
