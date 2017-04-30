from django.conf.urls import url

from .views import PostViewSet

urlpatterns = [
    url(r'posts', PostViewSet)
]
