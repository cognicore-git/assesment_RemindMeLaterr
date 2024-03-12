"""
Serializers for the Remind-me-later app.

This module defines serializers for converting Reminder objects into JSON representations.
"""

from rest_framework import serializers
from django.utils import timezone
from .models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    """
    Serializer for Reminder objects.

    This serializer converts Reminder model instances into JSON representations.

    Attributes:
        created_date (DateTimeField): The formatted representation of the created_date field.
    """

    created_date = serializers.DateTimeField(format='%y-%m-%d %H:%M-%S')

    class Meta:
        """
        Meta options for the ReminderSerializer.

        This Meta class defines options for the ReminderSerializer, specifying the associated model and fields to include in the serialization.

        Attributes:
            model (Model): The model class associated with the serializer.
            fields (list or tuple): The fields to include in the serialized representation of the model. Using '__all__' includes all fields of the model.
        """
        model = Reminder
        fields = '__all__'

    def validate(self, data):
        """
        Validate that none of the required fields are blank.
        """
        if not data.get('date'):
            raise serializers.ValidationError("Date field is required.")
        if not data.get('time'):
            raise serializers.ValidationError("Time field is required.")
        if not data.get('message'):
            raise serializers.ValidationError("Message field is required.")
        if not data.get('reminder_type'):
            raise serializers.ValidationError("Reminder type field is required.")
        return data

    def validate_date(self, value):
        """
        Validate the date format.

        Args:
            value (str): The value of the date field.

        Returns:
            str: The validated date value.

        Raises:serializers.ValidationError: If the date format is invalid.
        """
        try:
            # Convert date value to string and attempt to parse
            date_str = str(value)
            # Attempt to parse the date value
            timezone.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as exc:
            # If parsing fails, raise a validation error
            raise serializers.ValidationError("Invalid date format. Date should be in YYYY-MM-DD format.") from exc

        return value

    def validate_time(self, value):
        """
        Validate the time format.

        Args:
            value (str): The value of the time field.

        Returns:
            str: The validated time value.

        Raises:
            serializers.ValidationError: If the time format is invalid.
        """
        try:
             # Convert date value to string and attempt to parse
            time_str = str(value)
            # Attempt to parse the time value
            timezone.datetime.strptime(time_str, '%H:%M:%S')
        except ValueError as exc:
            # If parsing fails, raise a validation error
            raise serializers.ValidationError("Invalid time format. Time should be in HH:MM:SS format.") from exc

        return value
    