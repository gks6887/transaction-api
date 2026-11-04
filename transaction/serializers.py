from rest_framework import serializers
from .models import Transaction


class TransactionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ["user", "product", "payment_method"]

    def create(self, validated_data):
        user = self.context.get("request").user
        if user != validated_data["user"]:
            raise serializers.ValidationError({"user": "User does NOT match"})
        return super().create(validated_data)


class TransactionReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
        depth = 1
