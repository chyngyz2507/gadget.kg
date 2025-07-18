from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase, TokenRefreshView

from user.serializers import RegisterUserSerializer, MyTokenObtainPairSerializer, RefreshSerializer
from rest_framework.views import APIView

from user.tasks import send_message

User = get_user_model()


class RegisterUserAPIView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = User(email=email)
            user.set_password(password)
            user.save()
            send_message.delay(user.email, user.id)
        return Response(True)


class ActivateAPIView(APIView):
    permission_classes = []
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        user.is_active= True
        user.save()
        return Response(True)


class MyTokenObtainPairView(TokenViewBase):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = RefreshSerializer
