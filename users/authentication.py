from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Attempt to get the user by email
            user = get_user_model().objects.get(email=username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except get_user_model().DoesNotExist:
            return None
        except get_user_model().MultipleObjectsReturned:
            # Handle the case where there are multiple users with the same email
            return None

    def user_can_authenticate(self, user):
        # Ensure the user is active
        return user.is_active

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
