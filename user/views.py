from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from messages import LOGIN_INVALID_MESSAGE
from user.serializers import RegisterUserSerializer, LoginSerializer

User = get_user_model()

class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = User(email=email)
            user.set_password(password)
            user.save()
        return Response(True)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(**serializer.validated_data)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': LOGIN_INVALID_MESSAGE}, status=401)


class LogoutView(APIView):
    def post(self, request):
        if request.user:
            token = Token.objects.get(user=request.user)
            token.delete()
        return Response({'succes': 'успех'}, status=401)
