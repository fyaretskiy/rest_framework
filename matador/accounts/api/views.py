from django.db import IntegrityError
from django.utils.crypto import get_random_string
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import User
from .serializers import UserSerializer


class UserViewPermission(IsAuthenticated):

    def has_permission(self, request, view):
        """
        Allows POST of unauthenticated user.
        """
        if request.method == 'POST':
            return True
        else:
            return super().has_permission(request, view)


def get_username():
    while True:
        username = get_random_string(12)
        if not User.objects.filter(username=username).exists():
            return username


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserViewPermission]

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            user = User.objects.create_user(username=get_username())
            token = Token.objects.create(user=user)
            return Response({'token': token.key},
                            status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        User.objects.filter(id=request.user.pk).delete()
        Token.objects.filter(user=request.user).delete()
        return Response()

    def update(self, request, *args, **kwargs):
        new_username = request.data['username']
        try:
            user = request.user
            user.username = new_username
            user.save()
        except IntegrityError:
            return Response({"response": "Username already exists."},
                            status.HTTP_400_BAD_REQUEST, )
        else:
            return Response(self.serializer_class(user).data)

    def retrieve(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.request.user).data)
