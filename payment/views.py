from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action in ['create']:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Payment.objects.all()
        return Payment.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
