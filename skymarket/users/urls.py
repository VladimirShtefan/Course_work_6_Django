from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

# from djoser.views import UserViewSet
# from rest_framework.routers import SimpleRouter
#
# users_router = SimpleRouter()
#
# users_router.register("token", UserViewSet, basename="users")

urlpatterns = [
    path('', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view()),
    # path('', include(users_router.urls)),
    # path("", include(users_router.urls)),
]
