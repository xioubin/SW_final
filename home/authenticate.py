from django.contrib.auth.hashers import BasePasswordHasher
from django.contrib.auth.backends import BaseBackend
from .models import User_Info
# from IntellerMatrix.CommonUtilities.constants import Constants


class CustomerAuthenticationBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None):
        try:
            user = User_Info.objects.get(email=email)
        except User_Info.DoesNotExist:
            return None
        print(user.password, password, user.password == password)
        if user is not None and user.password == password:
            if user.is_active:
                return user
        return None


class PlainTextPassword(BasePasswordHasher):
    algorithm = "plain"

    def salt(self):
        return ''

    def encode(self, password, salt):
        assert salt == ''
        return password

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return OrderedDict([
            (_('algorithm'), self.algorithm),
            (_('hash'), encoded),
        ])
