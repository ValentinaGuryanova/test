from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserCreateSerializer


class IsActiveUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_active and request.user.is_active:
            return True
        return False


class UserCreateView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

