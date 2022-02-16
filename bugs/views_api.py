from rest_framework import viewsets
from .models import Ticket, Project, TicketComment
from .serializers import TicketSerializer, ProjectSerializer, TicketCommentSerializer
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView


class LoginView(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.order_by('-created_on')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.order_by('title')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TicketCommentViewSet(viewsets.ModelViewSet):
    serializer_class = TicketCommentSerializer
    queryset = TicketComment.objects.order_by('ticket')
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
