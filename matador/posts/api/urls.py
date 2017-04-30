from django.conf.urls import url

from .views import PostViewSet

urlpatterns = [
    url(r'posts/(?P<post_id>[0-9])', PostViewSet.as_view({'get': 'retrieve'}))
]
