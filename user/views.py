from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .serializers import UserCreateUpdateSerializer, UserReadSerializer
from permissions.is_owner import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    permission_classes = [IsAuthenticated, IsOwner]  # For Only Test purpose

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            self.serializer_class = UserCreateUpdateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        elif self.action == "list":
            return [IsAdminUser()]
        return super().get_permissions()