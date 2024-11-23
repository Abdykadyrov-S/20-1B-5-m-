# from django.shortcuts import render
# from rest_framework.generics import ListAPIView, CreateAPIView, \
# RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.
from apps.news.models import News
from apps.news.serializers import NewsSerializer
from apps.news.permissions import IsAdminOrReadOnly

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class NewsAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = Pagination
    permission_classes = (IsAdminOrReadOnly, )

"""
AllowAny - полный доступ  всем
IsAuthenticated - проверяет на авторизацию
IsAdminUser - только админ
IsAuthenticatedOrReadOnly - авторизованные пользователи получают полный доступ а не авторизованные только просмотр
"""


# class NewsListAPIView(ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsCreateAPIView(CreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsUpdateAPIView(UpdateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsRetrievAPIView(RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


