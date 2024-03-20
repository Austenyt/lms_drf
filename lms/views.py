from rest_framework import viewsets, generics
from rest_framework.response import Response

from lms.models import Course, Lesson
from users.permissions import IsModerator, IsOwnerOrReadOnly
from lms.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator | IsOwnerOrReadOnly]

    def list(self, request):
        return Response("List of courses")

    def retrieve(self, request, pk=None):
        return Response("Retrieve course details")

    def update(self, request, pk=None):
        return Response("Update course")

    def partial_update(self, request, pk=None):
        return Response("Partial update course")


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class LessonViewSet(viewsets.ViewSet):
    permission_classes = [IsModerator | IsOwnerOrReadOnly]

    def list(self, request):
        return Response("List of lessons")

    def retrieve(self, request, pk=None):
        return Response("Retrieve lesson details")

    def update(self, request, pk=None):
        return Response("Update lesson")

    def partial_update(self, request, pk=None):
        return Response("Partial update lesson")
