from rest_framework import serializers

from lms.models import Course, Lesson, Subscription
from lms.validators import LessonCustomValidator


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField()

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonCustomValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_num_lessons(self, instance):
        return instance.lesson_set.all().count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        user = request.user
        return Subscription.objects.filter(user=user, course=obj).exists()

    class Meta:
        model = Course
        fields = ['id', 'name', 'num_lessons', 'description', 'is_subscribed']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
