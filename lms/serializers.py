from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import validate_youtube_url
from users.serializers import SubscriptionSerializer


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validate_youtube_url])
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = SubscriptionSerializer(many=True, read_only=True, source='subscription_set')

    def get_num_lessons(self, instance):
        return instance.lesson_set.all().count()

    class Meta:
        model = Course
        fields = ('id', 'name', 'num_lessons')
