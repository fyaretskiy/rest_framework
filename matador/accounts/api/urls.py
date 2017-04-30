from django.conf.urls import url, include

from .views import UserViewSet

urlpatterns = [
    url(r'users', UserViewSet)
]