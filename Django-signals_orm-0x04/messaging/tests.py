from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message, MessageHistory, Notification

User = get_user_model()

class NotificationSignalTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='pass')
        self.receiver = User.objects.create_user(username='receiver', password='pass')

    def test_notification_created_on_message(self):
        msg = Message.objects.create(sender=self.sender, receiver=self.receiver, content="Hello!")
        
        notif = Notification.objects.filter(user=self.receiver, message=msg)
        self.assertEqual(notif.count(), 1)

    def test_history_logged_on_message_edit(self):
        msg = Message.objects.create(sender=self.sender, receiver=self.receiver, content="First message")
        msg.content = "Edited message"
        msg.save()
        msg.refresh_from_db()
        self.assertTrue(msg.edited)
        history = MessageHistory.objects.filter(message=msg)
        self.assertEqual(history.count(), 1)
        self.assertEqual(history.first().old_content, "First message")
        self.assertEqual(history.first().edited_by, self.sender)