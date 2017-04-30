import os

from django.conf import settings
from django.conf.urls import include, url

urlpatterns = []

for app in settings.LOCAL_APPS:
    url_file = os.path.join(app, 'api', 'urls.py')
    if os.path.exists(url_file):
        urlpatterns += [url(r'^api/v1/',
                            include('{app}.api.urls'.format(app=app)))]
