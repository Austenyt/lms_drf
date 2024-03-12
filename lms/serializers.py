from rest_framework import serializers

from lms.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()

    def get_num_lessons(self, course):
        return course.lesson_set.count() if course.lesson_set.exists() else 0

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'num_lessons']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
