from rest_framework import viewsets, mixins, exceptions
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionReadSerializer, TransactionCreateSerializer


class TransactionViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionReadSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "POST":
            self.serializer_class = TransactionCreateSerializer
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Transaction.objects.filter(user__id=self.request.user.id)
        return super().get_queryset()
