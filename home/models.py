from django.db import models
from django.conf import settings

User_Info = settings.AUTH_USER_MODEL
Login_Info = settings.AUTH_USER_MODEL
Book_Info = settings.AUTH_USER_MODEL

# class User_InfoManager(BaseUserManager):
#     def create_user(self, email, username, profile_picture, password=None, is_admin=False, is_staff=False, is_active=True):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
#         if not username:
#             raise ValueError("User must have a username")

#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         user.username = username
#         user.set_password(password)  # change password to hash
#         user.profile_picture = profile_picture
#         user.admin = is_admin
#         user.staff = is_staff
#         user.active = is_active
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
#         if not username:
#             raise ValueError("User must have a username")

#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         user.username = username
#         user.set_password(password)
#         user.admin = True
#         user.staff = True
#         user.active = True
#         user.save(using=self._db)
#         return user


# class User_Info(AbstractBaseUser):
#     USERNAME_FIELD = 'email'
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField(unique=True, max_length=100)
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_(
#             'Designates whether the user can log into this admin site.'),
#     )
#     objects = User_InfoManager()

#     REQUIRED_FIELDS = ['username', 'password']


class User_Info(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)

class Login_Info(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Book_Info(models.Model):
    room = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    participant = models.CharField(max_length=100)
   

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

    room = models.IntegerField(choices=ROOM_CHOICES)

    title = models.CharField(max_length=150)

    date = models.DateTimeField()
    time = models.IntegerField(choices=TIME_CHOICES)

    # class Meta:
    #     unique_together = ((date, time, room),)
