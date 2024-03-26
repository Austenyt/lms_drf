from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from lms.models import Lesson, Course, Subscription
from users.models import User


class LessonCrudTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='test_course', description='test_description')
        self.lesson = Lesson.objects.create(name='test_lesson', description='test_description', course=self.course)

    def test_create_lesson(self):
        url = reverse('lms:lesson-create')
        data = {'name': 'Test Lesson', 'description': 'Test Description', 'course': self.course.id}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Lesson.objects.count(), 1)  # Проверяем увеличение количества уроков

    def test_update_lesson(self):
        url = reverse('lms:lesson-update', kwargs={'pk': self.lesson.id})
        data = {'name': 'Updated Lesson', 'description': 'Updated Description', 'course': self.course.id}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        updated_lesson = Lesson.objects.get(id=self.lesson.id)
        self.assertEqual(updated_lesson.name, 'Updated Lesson')

    def test_delete_lesson(self):
        url = reverse('lms:lesson-delete', kwargs={'pk': self.lesson.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)  # Проверяем удаление урока


class SubscriptionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='test_course', description='test_description')

    def test_subscription_toggle(self):
        url = reverse('lms:subscription')
        data = {'course_id': self.course.id}

        # Добавляем подписку
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

        # Удаляем подписку
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

        # Проверяем обработку некорректного course_id
        data['course_id'] = 999  # Несуществующий ID курса
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(str(response.data['detail']), 'Not found.')
