from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscribe
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")
        self.course = Course.objects.create(
            name="Экономика", description="обучение финансам", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="Экономика в производстве",
            description="тонкости экономических производств",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "name": "test lesson",
            "description": "test lesson description",
            "video_url": "https://www.youtube.com/watch?v=dsadklr5",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "test lesson",
            "description": "test lesson description",
            "video_url": "https://www.youtube.com/watch?v=gasdsldak9",
            "course": self.course.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "test lesson")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": None,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview_image": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name="Test Course",
            description="Test Course Description",
        )
        self.lesson = Lesson.objects.create(
            name="Test Lesson",
            description="Test Lesson Description",
            course=self.course,
        )
        self.url = reverse("materials:course_subscribe")

    def test_subscribe_create(self):
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(self.url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(temp_data.get("message"), "Подписка добавлена")
        self.assertEqual(Subscribe.objects.all().count(), 1)

    def test_subscribe_delete(self):
        Subscribe.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(temp_data.get("message"), "Подписка удалена")
        self.assertEqual(Subscribe.objects.all().count(), 0)
