from rest_framework.test import APITestCase
from rest_framework import status

from users.models import Subscription, User
from .models import Lesson
from .serializers import LessonSerializer


class LessonAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.lesson_data = {'name': 'Test Lesson', 'description': 'This is a test lesson description.'}
        self.lesson = Lesson.objects.create(owner=self.user, **self.lesson_data)

    def test_create_lesson(self):
        response = self.client.post('/api/lessons/', self.lesson_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        response = self.client.get(f'/api/lessons/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, LessonSerializer(self.lesson).data)

    def test_update_lesson(self):
        updated_data = {'name': 'Updated Lesson', 'description': 'Updated lesson description.'}
        response = self.client.put(f'/api/lessons/{self.lesson.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.name, updated_data['name'])

    def test_delete_lesson(self):
        response = self.client.delete(f'/api/lessons/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

    def test_subscription_functionality(self):
        course_id = 1
        response = self.client.post('/api/subscribe/', {'course_id': course_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course_id=course_id).exists())
