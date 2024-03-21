from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from users.models import Subscription
from .models import Course, Lesson


class LessonSubscriptionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.admin_user = User.objects.create_superuser(username='adminuser', password='adminpass')
        self.course = Course.objects.create(title='Test Course', description='Test Description')
        self.lesson = Lesson.objects.create(title='Test Lesson', course=self.course)
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)

    def test_create_lesson_as_owner(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/lessons/', {'title': 'New Lesson', 'course': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_lesson_as_owner(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(f'/lessons/{self.lesson.id}/', {'title': 'Updated Lesson'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson_as_owner(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/lessons/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_lesson_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post('/lessons/', {'title': 'New Lesson', 'course': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscribe_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/subscriptions/', {'course': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unsubscribe_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/subscriptions/{self.subscription.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)