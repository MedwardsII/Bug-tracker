from rest_framework import serializers
from .models import Ticket, Project, TicketComment


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'description',
            'is_resolved',
            'priority',
            'created_on',
            'last_updated',
            'project',
            'creator'
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title']

class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'comment',
            'creator',
            'ticket',
            'created_on'
        ]