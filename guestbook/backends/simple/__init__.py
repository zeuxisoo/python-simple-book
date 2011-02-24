from django.contrib.auth.models import User

from registration.backends.default import DefaultBackend
from registration import signals
from guestbook.forms import RegisterForm

class SimpleBackend(DefaultBackend):
    """
    create a active user, no need to verfy email.
    """
    def register(self, request, **kwargs):
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
        new_user = User.objects.create_user(username, email, password)
        signals.user_registered.send(
        	sender=self.__class__,
			user=new_user,
			request=request
		)
        return new_user

    def get_form_class(self, request):
        return RegisterForm