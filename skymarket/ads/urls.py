from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')
ads_router.register('ads/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
]
