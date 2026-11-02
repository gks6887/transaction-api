from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserCreateUpdateSerializer, UserReadSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]  # For Only Test purpose

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            self.serializer_class = UserCreateUpdateSerializer
        elif self.request.method == "GET":
            self.serializer_class = UserReadSerializer
        return super().get_serializer_class()