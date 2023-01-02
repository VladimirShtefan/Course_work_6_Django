from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView


users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users_router.urls)),
    path('api/', include('users.urls')),
    path('refresh/', TokenRefreshView.as_view()),
    path('api/', include('ads.urls')),
    path('redoc/', include('redoc.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
