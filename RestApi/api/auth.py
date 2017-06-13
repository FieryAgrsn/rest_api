from api.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from rest_framework.authentication import SessionAuthentication


class SuperUserSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        print("fuck")
        # Get the underlying HttpRequest object
        request = request._request
        user = getattr(request, 'user', None)
        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active or not user.is_superuser:
            return None

        self.enforce_csrf(request)

        # CSRF passed with authenticated user
        return (user, None)

class Authentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        print("shit")
        if not username: # no username passed in request headers
            return None # authentication did not succeed

        try:
            user = User.objects.get(username=username) # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist

        return (user, None) # authentication successful