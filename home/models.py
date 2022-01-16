from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)


class Reservation(models.Model):

    ROOM_CHOICES = [
        (0, "ROOM 1"),
        (1, "ROOM 2"),
        (2, "ROOM 3"),
        (3, "ROOM 4"),
        (4, "ROOM 5"),
    ]

    TIME_CHOICES = [
        (0, "8-9"),
        (1, "9-10"),
        (2, "10-11"),
        (3, "11-12"),
        (4, "12-13"),
        (5, "13-14"),
        (1, "14-15"),
        (2, "16-17")
    ]

    organizer = models.ForeignKey(
        User,
        related_name="organized_reservations",
        on_delete=models.CASCADE
    )
    invitees = models.ManyToManyField(
        User
    )

    room = models.IntegerField(choices=ROOM_CHOICES)

    title = models.CharField(max_length=150)

    date = models.DateTimeField()
    time = models.IntegerField(choices=TIME_CHOICES)

    # class Meta:
    #     unique_together = ((date, time, room),)
