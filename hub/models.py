from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    """
    Defines the chatRoom model to host users and allow engagement
    """
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=User, blank=True)

    def get_online_count(self):
        """
        Return number of members online
        """
        return self.online.count()

    def join(self, user):
        """
        Allow a user to join a chat room
        """
        self.online.add(user)
        self.save()

    def leave(self, user):
        """
        Remove a user to leave the chat room when disconnected
        """
        self.online.remove(user)
        self.save()

    def __str__(self):
        """
        String representation of Room model
        """
        return f'{self.name} ({self.get_online_count()})'


class Message(models.Model):
    """
    Defines the Message model to allow users to send and receive
    messages
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the message model
        """
        return f'{self.user.username}: {self.content} [{self.timestamp}]'
