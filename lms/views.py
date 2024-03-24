from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, Subscription
from lms.pagination import CourseLessonPagination
from lms.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsOwnerOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CourseLessonPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Пользователь может редактировать только свои уроки

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CourseLessonPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    name = 'lesson-update'


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class SubscriptionView(APIView):
    serializer_class = SubscriptionSerializer

    @staticmethod
    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, pk=course_id)

        if Subscription.objects.filter(user=user, course=course).exists():
            Subscription.objects.filter(user=user, course=course).delete()
            message = 'Subscription removed'
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Subscription added'

        return Response({"message": message})
