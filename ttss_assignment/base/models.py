from django.db import models
from django.contrib.auth.models import User


class RoomActivity(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # someone has to host the room
    roomActivity = models.ForeignKey(RoomActivity, on_delete=models.SET_NULL, null=True)  # if a room activity is
    # deleted, set it to null. Allow it to be set to null.
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)  # allows database description and it's submitted form to be
    # null
    participants = models.ManyToManyField(User, related_name='participants', blank=True) #store all the users active in a room
    updated = models.DateTimeField(auto_now=True)  # takes a timestamp of when this model is updated
    created = models.DateTimeField(
        auto_now_add=True)  # takes a timestamp of when this model is first created (this value never changes)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # One-to-many relationship where if a user is deleted,
    # all messages (children) by them are deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # if the parent (Room) is deleted, deleted all the
    # children (the messages)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]  # trim it down to only include the first 50 characters of the message
