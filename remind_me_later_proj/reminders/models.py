"""
Models for the Remind-me-later app.

This module defines the database models for storing reminders.
"""
from django.db import models

# Create your models here.
class Reminder(models.Model):
    """
    Model to store reminders.

    Attributes:
        id (AutoField): The primary key of the reminder.
        date (DateField): The date of the reminder.
        time (TimeField): The time of the reminder.
        message (TextField): The reminder message.
        reminder_type (CharField): The type of reminder (e.g., SMS, Email).
        created_date (DateTimeField): The date and time when the reminder was created.
    """
    id=models.AutoField(primary_key=True)
    date=models.DateField(blank=False,null=False)
    time=models.TimeField(blank=False,null=False)
    message=models.TextField(blank=False,null=False)
    reminder_type=models.CharField(max_length=255,blank=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadata options for the Reminder model.

        This Meta class defines metadata options for 
        the Reminder model, such as database table name 
        and manageability.

        Attributes:
            manage (bool): A boolean indicating whether this 
            model should be managed by Django's database backend.
            db_table (str): The name of the database table to 
            use for storing Reminder objects.
        """
        managed = True
        db_table = 'tbl_reminders_queue'

    def __str__(self):
        return str(self.message)
