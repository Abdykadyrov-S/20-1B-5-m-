from django.urls import path

from .views import UserListAPIView, UserCreateAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name="api users list"),
    path('register/', UserCreateAPIView.as_view(), name="api users register"),
]