from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.apps import UsersConfig
from users.views import (PaymentViewSet, UserCreateAPIView)


app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payment", PaymentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('register/',UserCreateAPIView.as_view(), name= 'register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
] + router.urls