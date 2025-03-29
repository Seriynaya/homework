from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .models import Payment, User
from .serializers import PaymentSerializer
from users.serializers import UserSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('paid_course','paid_lesson', "payment_method")
    ordering_fields = ('payment_date',)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer