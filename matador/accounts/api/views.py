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

    def update(self, request, *args, **kwargs):
        """Skipping because user has no data to update."""

    def destroy(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            User.objects.filter(id=request.user.pk).delete()
            Token.objects.filter(user=request.user).delete()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response()

    # def list(self, request, *args, **kwargs):
    #     # fixme view users list from the data source
    #     data = self.serializer_class(self.queryset, many=True).data
    #     return Response(data)
    #
    # def get_object(self):
    #     pass
