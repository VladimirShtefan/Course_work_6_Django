from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdListSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    max_page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.select_related('author').all()
    serializer_classes = {
        'list': AdListSerializer,
        'retrieve': AdSerializer,
    }
    default_serializer_class = AdSerializer
    pagination_class = AdPagination

    permission_classes_by_action = {
        'default': (AllowAny,),
        'create': (AllowAny,),
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'update': (AllowAny,),
        'destroy': (AllowAny,),
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes_by_action["default"]]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('user_comment').select_related('ad_comment').all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    permission_classes_by_action = {
        'default': (AllowAny,),
        'create': (AllowAny,),
        'list': (AllowAny,),
        'retrieve': (AllowAny,),
        'update': (AllowAny,),
        'destroy': (AllowAny,),
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes_by_action["default"]]

