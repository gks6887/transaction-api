from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import serializers


class UserCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def validate_password_input(self, password):
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

    def create(self, validated_data):
        self.validate_password_input(validated_data["password"])
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("password") is not None:
            self.validate_password_input(validated_data["password"])
            validated_data["password"] = make_password(validated_data["password"])

        return super().update(instance, validated_data)


class UserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "date_joined", "is_active", "is_staff"]