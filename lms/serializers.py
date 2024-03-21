from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_num_lessons(self, instance):
        return instance.lesson_set.all().count()

    class Meta:
        model = Course
        fields = ('id', 'name', 'num_lessons')
