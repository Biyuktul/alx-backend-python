from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from .models import User, Conversation, Message
from .permissions import IsParticipant

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing conversations.
    Provides CRUD operations for conversations.
    Access is restricted to participants only.
    """
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] 
    search_fields = ['participants__username']
    ordering_fields = ['created_at']
    permission_classes = [IsAuthenticated, IsParticipant]

    def get_queryset(self):
        # Only show conversations where the request user is a participant
        return Conversation.objects.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation with participants.
        Expects a list of user IDs in 'participant_ids'.
        """
        participant_ids = request.data.get('participant_ids', [])
        if not participant_ids or not isinstance(participant_ids, list):
            return Response({'error': 'participant_ids must be a list of user IDs.'}, status=status.HTTP_400_BAD_REQUEST)
        # Validate that all users exist
        users = User.objects.filter(user_id__in=participant_ids)
        if users.count() != len(participant_ids):
            return Response({'error': 'One or more participants not found.'}, status=status.HTTP_400_BAD_REQUEST)
        conversation = Conversation.objects.create()
        conversation.participants.set(users)
        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing messages.
    Provides CRUD operations for messages within conversations.
    Access is restricted to participants only.
    """
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['message_body', 'sender__username']
    ordering_fields = ['sent_at']
    permission_classes = [IsAuthenticated, IsParticipant]

    def get_queryset(self):
        # Only show messages in conversations where the user is a participant
        return Message.objects.filter(conversation__participants=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Send a message to an existing conversation.
        Expects 'conversation', 'sender', and 'message_body' in the request data.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)