from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.news.views import NewsAPI

router = DefaultRouter()
router.register("api_news", NewsAPI, basename='api-news')

urlpatterns = [

]

urlpatterns += router.urls

# from apps.news.views import NewsListAPIView, NewsCreateAPIView, \
# NewsUpdateAPIView, NewsDeleteAPIView, NewsRetrievAPIView

# urlpatterns = [
#     path("news_list", NewsListAPIView.as_view(), name='list_api'),
#     path("create/", NewsCreateAPIView.as_view(), name='create news'),
#     path("update/<int:pk>", NewsUpdateAPIView.as_view(), name='delete news'),
#     path("<int:pk>", NewsRetrievAPIView.as_view(), name='retriev_news'),
#     path("delete/<int:pk>", NewsDeleteAPIView.as_view(), name='delete_news')
# ]
