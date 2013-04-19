incuna-internal-social-auth
===========================

Django Social Auth extras for the Incuna internal apps.

Setting up your apps google Oauth2
----------------------------------

goto ``https://code.google.com/apis/console``

* Click the drop down
* Click on the create link
* Follow setup instructions

After the Oauth2 has been setup place the GOOGLE_OAUTH2_CLIENT_ID &
GOOGLE_OAUTH2_CLIENT_SECRET into your apps environment variables::

    export GOOGLE_OAUTH2_CLIENT_ID='your-apps-client-id'
    export GOOGLE_OAUTH2_CLIENT_SECRET='your-apps-client-secret'

If you get stuck follow Hickman's rather useful blog post::
http://ghickman.co.uk/2012/07/22/setup-single-sign-on-in-django-using-google-oauth2.html

Installation
------------

Run ``pip install incuna-internal-social-auth``.

Add ``'internal_social_auth',`` & ``'social_auth',`` to ``INSTALLED_APPS`` in your ``settings.py`` and the Social Auth settings::

    from django.core.urlresolvers import reverse_lazy    

    # Social auth
    AUTHENTICATION_BACKENDS = (
        'social_auth.backends.google.GoogleOAuth2Backend',
        'django.contrib.auth.backends.ModelBackend',
    )

    GOOGLE_OAUTH2_CLIENT_ID = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
    GOOGLE_OAUTH2_CLIENT_SECRET = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']
    GOOGLE_WHITE_LISTED_DOMAINS = ['incuna.com']
    SOCIAL_AUTH_USER_MODEL = 'auth.User'

    LOGIN_URL = reverse_lazy('socialauth_begin', kwargs={'backend': 'google-oauth2'})
    LOGIN_REDIRECT_URL = '/'


Add the urls to your ``urls.py``::

    from internal_social_auth.views import AuthComplete, LoginError

    url(r'^complete/(?P<backend>[^/]+)/$', AuthComplete.as_view()),
    url(r'^login-error/$', LoginError.as_view()),
    url(r'', include('social_auth.urls')),
