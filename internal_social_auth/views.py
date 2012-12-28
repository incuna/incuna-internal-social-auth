import logging

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.encoding import force_text
from django.views.generic.base import View
from social_auth.exceptions import AuthFailed
from social_auth.views import complete


logger = logging.getLogger(__name__)


class AuthComplete(View):
    def get(self, request, *args, **kwargs):
        backend = kwargs.pop('backend')
        try:
            return complete(request, backend, *args, **kwargs)
        except AuthFailed as e:
            logger.error(e)
            messages.error(request, self.get_error_message())
            return HttpResponseRedirect(self.get_faiure_url())

        def get_error_message(self):
            if self.error_message:
                return self.error_message
            return "Your Google Apps domain isn't authorized for this app"

        def get_failure_url(self):
            if self.failure_url:
                return force_text(self.failure_url)
            return '/'


class LoginError(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=401)
