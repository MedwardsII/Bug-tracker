from django.forms import ModelForm
from .models import Ticket, TicketComment
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
import os

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'description',
            'is_resolved',
            'priority',
            'project'
        ]

class TicketCommentForm(ModelForm):
    class Meta:
        model = TicketComment
        fields = [
            'comment'
        ]

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'value': os.getenv('DEFAULT_LOGIN_USERNAME') or ''
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'value': os.getenv('DEFAULT_LOGIN_PASSWORD') or ''
        }
))