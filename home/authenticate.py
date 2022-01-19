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
