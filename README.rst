incuna-internal-social-auth
===========================

Django Social Auth extensions for the Incuna internal apps.

Installation
------------

Run ``pip install incuna-internal-social-auth``.

Add ``'internal_social_auth'`` to ``INSTALLED_APPS`` in your ``settings.py`` and the Social Auth settings::

    # Social auth
    GOOGLE_OAUTH2_CLIENT_ID = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
    GOOGLE_OAUTH2_CLIENT_SECRET = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']
    GOOGLE_WHITE_LISTED_DOMAINS = ['incuna.com']
    SOCIAL_AUTH_USER_MODEL = 'auth.User'


Add these two urls to your ``urls.py``::

    url(r'^complete/(?P<backend>[^/]+)/$', views.AuthComplete.as_view()),
    url(r'^login-error/$', views.LoginError.as_view()),

