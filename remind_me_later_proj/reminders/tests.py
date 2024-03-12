"""
Tests for the Reminder API.

This module contains test cases to verify 
the behavior of the Reminder API endpoints. 
The Reminder API allows users to create reminders 
with a specific date, time, message, and reminder 
type (e.g., SMS, Email).
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Reminder

class ReminderAPITestCase(TestCase):
    """
    Test case for the Reminder API.

    This test case class verifies the behavior of the 
    Reminder API endpoints.
    """

    def setUp(self):
        """
        Set up the test case.

        This method is called before each test method execution.
        """
        self.client = APIClient()

    def test_create_reminder(self):
        """
        Test creation of a new reminder.

        This test method verifies that a new reminder can be 
        successfully created via the API.
        """
        # Test valid reminder creation
        data = {
            'date': '2024-03-12',
            'time': '08:00:00',
            'message': 'Test reminder message',
            'reminder_type': 'SMS'
        }
        url = reverse('reminder-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 1)
        self.assertEqual(Reminder.objects.get().message, 'Test reminder message')

        # Check if created_date is set to the current time
        created_reminder = Reminder.objects.first()
        self.assertIsNotNone(created_reminder.created_date)

        # Test creation with missing required fields
        missing_fields_data = {
            'date': '2024-03-12',
            'time': '08:00:00',
            # Missing 'message' field intentionally
            'reminder_type': 'SMS'
        }
        response = self.client.post(url, missing_fields_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Reminder.objects.count(), 1)  # Database should not change

        # Test creation with invalid date format
        invalid_date_data = {
            'date': '2024/03/12',  # Invalid date format
            'time': '08:00:00',
            'message': 'Test reminder message',
            'reminder_type': 'SMS'
        }
        response = self.client.post(url, invalid_date_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Reminder.objects.count(), 1)  # Database should not change

        # Test creation with invalid time format
        invalid_time_data = {
            'date': '2024-03-12',
            'time': '08:00 pm',  # Invalid time format
            'message': 'Test reminder message',
            'reminder_type': 'SMS'
        }
        response = self.client.post(url, invalid_time_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Reminder.objects.count(), 1)  # Database should not change
