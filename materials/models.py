from django.db import models
from config.settings import AUTH_USER_MODEL

class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="courses/previews",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    description = models.TextField(
        max_length=150,
        verbose_name="Описание курса",
        help_text="Введите описание",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель курса",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

        def __str__(self):
            return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        max_length=150,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="lessons/previews",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    video_url = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Загрузите ссылку на видео",
    )
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, verbose_name="Курс", blank=True, null=True, related_name='lessons'
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель урока",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

        def __str__(self):
            return self.name
