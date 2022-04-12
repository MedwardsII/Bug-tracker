from django.test import TestCase
from django.db import models
from .models import Project, Ticket, TicketComment
from django.contrib.auth.models import User


class TestProjectModel(TestCase):
    '''Test the project model.'''
    def setUp(self) -> None:
        self.project = Project(
            title='Project Name'
        )
    def test_create_project(self):
        self.assertIsInstance(self.project, Project)
    def test_str_representation(self):
        self.assertEquals(str(self.project), 'Project Name')

class TestTicketModel(TestCase):
    '''Test the ticket model.'''
    def setUp(self) -> None:
        self.project = Project(
            title='Ticket Name'
        )
        self.user = User(
            username='Username',
            password='password'
        )
        self.ticket = Ticket(
            description='Ticket Description',
            is_resolved=False,
            priority='Urgent',
            created_on=models.DateTimeField(
                auto_now_add=True,
            ),
            last_updated=models.DateTimeField(
                auto_now_add=True,
            ),
            project=self.project,
            creator=self.user,
        )
    def test_create_ticket(self):
        self.assertIsInstance(self.ticket, Ticket)
    def test_str_representation(self):
        self.assertEquals(str(self.ticket), 'Ticket Description')

class TestTicketCommentModel(TestCase):
    '''Test the ticket comment model.'''
    def setUp(self) -> None:
        self.project = Project(
            title='Ticket Name'
        )
        self.user = User(
            username='Username',
            password='password'
        )
        self.ticket = Ticket(
            description='Ticket Description',
            is_resolved=False,
            priority='Urgent',
            created_on=models.DateTimeField(
                auto_now_add=True,
            ),
            last_updated=models.DateTimeField(
                auto_now_add=True,
            ),
            project=self.project,
            creator=self.user,
        )
        self.ticket_comment = TicketComment(
            comment='This is a comment.',
            creator=self.user,
            ticket=self.ticket,
            created_on=models.DateTimeField(
                auto_now_add=True,
            )
        )
    def test_create_ticketcomment(self):
        self.assertIsInstance(self.ticket_comment, TicketComment)
