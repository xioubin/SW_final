from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
# User_Info = settings.AUTH_USER_MODEL


class User_InfoManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, username, password, is_superuser=False, is_staff=False, is_active=True, **other_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email=self.normalize_email(email)
        )
        print()
        user.username = username
        user.set_password(password)  # change password to hash
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None,  **other_fields):
        return self.create_user(email=email, username=username, password=password, is_superuser=True,  is_staff=True, is_active=True, **other_fields)


class User_Info(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    is_superadmin = models.BooleanField(_('is_superadmin'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(default=False)
    objects = User_InfoManager()

    REQUIRED_FIELDS = ['username']


# class User_Info(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField(unique=True, max_length=100)


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
        User_Info,
        related_name="organized_reservations",
        on_delete=models.CASCADE
    )
    invitees = models.ManyToManyField(
        User_Info
    )

    # auto_increment_id = models.AutoField(primary_key=True)

    room = models.IntegerField(choices=ROOM_CHOICES)

    title = models.CharField(max_length=150)

    date = models.DateField()
    time = models.IntegerField(choices=TIME_CHOICES)

    # class Meta:
    #     unique_together = ((date, time, room),)


class ErrorReport(models.Model):
    content = models.CharField(max_length=500)
