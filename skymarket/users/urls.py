from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view()),
]
