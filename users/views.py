from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsModerator
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = []  # Для создания пользователей доступно всем
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]  # Для просмотра списка пользователей требуется аутентификация
        else:
            permission_classes = [IsModerator]  # Для других действий требуются права модератора
        return [permission() for permission in permission_classes]
