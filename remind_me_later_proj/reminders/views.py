"""
Views for the Remind-me-later app.

This module defines views for handling API requests related to reminders.
"""

from rest_framework import generics,status
from rest_framework.response import Response
from django.utils import timezone
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderCreateView(generics.GenericAPIView):
    """
    View for creating reminders.

    This view handles POST requests to create new reminder objects.

    Attributes:
        queryset (QuerySet): The queryset to retrieve Reminder objects.
        serializer_class (Serializer): The serializer class to use for Reminder objects.
    """

    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def post(self, request):
        """
        Handle POST requests to create new reminder objects.

        Args:
            request (HttpRequest): The POST request containing reminder data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The HTTP response containing the created 
            reminder data or error messages.
        """

        # Initialize request_data with request.data and add created_date
        request_data = {
            'date': request.data.get('date'),
            'time': request.data.get('time'),
            'message': request.data.get('message'),
            'reminder_type': request.data.get('reminder_type'),
            'created_date': timezone.now(),  # Add created_date with current time
        }
        # Initialize the serializer with request data
        serializer = self.get_serializer(data=request_data)
        # Check if serializer data is valid
        if serializer.is_valid():
            # Save the serializer data (create new reminder)
            serializer.save()
            # Return success response with created reminder data
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return error response with serializer errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
