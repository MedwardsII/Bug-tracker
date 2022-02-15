from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    '''Project data model'''
    title = models.CharField(
        max_length=50
    )
    def __str__(self):
        return str(self.title)

class Ticket(models.Model):
    '''Ticket data model'''
    class PriorityLevel(models.TextChoices):
        '''Priority level class'''
        LOW = 'Low'
        URGENT = 'Urgent'
        CRITICAL = 'Critical'
    description = models.TextField(
        max_length=500,
        help_text='Brief description of the bug.'
    )
    is_resolved = models.BooleanField(
        'Resolved',
        default=False
    )
    priority = models.CharField(
        max_length=8,
        choices=PriorityLevel.choices,
        default=PriorityLevel.LOW,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='Date ticket was created.'
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text='Date ticket was last modified.'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        help_text="The project this ticket is associated with."
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return str(self.description)

class TicketComment(models.Model):
    '''Ticket comment model class'''
    comment = models.TextField(
        max_length=500
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='Date ticket comment was created.'
    )
