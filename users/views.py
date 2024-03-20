from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsModerator
from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']


class UserViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsModerator]
        return [permission() for permission in self.permission_classes]

    # Методы для операций с уроками
    @action(detail=True, methods=['get'])
    def lesson_view(self, request, pk=None):
        # Логика просмотра урока
        return Response("Viewing lesson")

    @action(detail=True, methods=['put'])
    def lesson_update(self, request, pk=None):
        # Логика обновления урока
        return Response("Updating lesson")

    # Методы для операций с курсами
    @action(detail=True, methods=['get'])
    def course_view(self, request, pk=None):
        # Логика просмотра курса
        return Response("Viewing course")

    @action(detail=True, methods=['put'])
    def course_update(self, request, pk=None):
        # Логика обновления курса
        return Response("Updating course")
