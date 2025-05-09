from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscribe


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "description", "count_lessons", "lessons")


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"
