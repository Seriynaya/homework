from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    HomePageView,
    LessonCreateApiView,
    LessonDestroyApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView, SubscribeAPIView,
)

app_name = MaterialsConfig.name
router = SimpleRouter()
router.register("", CourseViewSet)
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("lessons/", LessonListApiView.as_view(), name="lesson_list"),
    path("lessons/<int:pk>", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyApiView.as_view(),
        name="lesson_delete",
    ),
    path(
        "lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"
    ),
    path("subscribe/", SubscribeAPIView.as_view(), name="course_subscribe"),
]
urlpatterns += router.urls
