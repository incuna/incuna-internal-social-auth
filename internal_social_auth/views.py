import logging

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
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
            messages.error(request, "Your Google Apps domain isn't authorized for this app")
            return HttpResponseRedirect('/')


class LoginError(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=401)


