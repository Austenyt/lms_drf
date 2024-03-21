from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import LessonLinkValidator
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            LessonLinkValidator(allowed_domain='youtube.com')
        ]


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_num_lessons(self, instance):
        return instance.lesson_set.all().count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = ['id', 'name', 'num_lessons', 'description', 'is_subscribed']
