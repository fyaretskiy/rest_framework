from django.utils.crypto import get_random_string
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from ..models import User
from .serializers import UserSerializer


def get_username():
    while True:
        username = get_random_string(12)
        if not User.objects.filter(username=username).exists():
            return username


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        if not request.user.is_authenticated():
            user = User.objects.create_user(username=get_username())
            token = Token.objects.create(user=user)
            return Response({'token': token.key})

        return Response(status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    def get_object(self):
        pass
