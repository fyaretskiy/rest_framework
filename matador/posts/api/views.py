from rest_framework import viewsets, status
from rest_framework.response import Response

from ..models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            post = Post.get_post_for_user(kwargs['post_id'], request.user)
            return Response(self.serializer_class(post).data)

        return Response(status=status.HTTP_403_FORBIDDEN)
