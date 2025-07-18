import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


logger = logging.getLogger(__name__)
class GmailAPIExeption(APIException):
    status_code = 400
    default_detail = {"message": "Регистрация только по gmail"}


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    def validate(self, attrs):
        email: str = attrs.get("email")
        user = User.objects.filter(email=email)
        if not email.endswith("@gmail.com"):
            raise GmailAPIExeption()
        if user.exists():
            raise serializers.ValidationError("Этот емейл уже занят!!!")
        password1 = attrs.pop("password1")
        password2 = attrs.pop("password2")
        if password1 == password2:
            attrs["password"] = password1
        else:
            raise serializers.ValidationError("Пароли не совпадают!!!")
        return attrs


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=8, write_only=True)

class MyTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        refresh["email"] = self.user.email
        refresh["role"] = self.user.role
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data


class RefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs) -> dict[str, str]:
        refresh = self.token_class(attrs["refresh"])
        logger.error(refresh)
        user_id = refresh.payload.get(api_settings.USER_ID_CLAIM, None)
        if user_id and (
                user := get_user_model().objects.get(
                    **{api_settings.USER_ID_FIELD: user_id}
                )
        ):
            if not api_settings.USER_AUTHENTICATION_RULE(user):
                raise AuthenticationFailed(
                    self.error_messages["no_active_account"],
                    "no_active_account",
                )
        user = User.objects.get(id=user_id)

        refresh.set_jti()
        refresh.set_exp()
        refresh.set_iat()
        refresh["email"] = user.email
        data = {"access": str(refresh.access_token), "refresh":  str(refresh)}

        return data
