incuna-internal-social-auth
===========================

Django Social Auth extensions for the Incuna internal apps.

Installation
------------

Run ``pip install incuna-internal-social-auth``.

Add ``'internal_social_auth'`` to ``INSTALLED_APPS`` in your ``settings.py``.

Add these two urls to your ``urls.py``::

    url(r'^complete/(?P<backend>[^/]+)/$', views.AuthComplete.as_view()),
    url(r'^login-error/$', views.LoginError.as_view()),

