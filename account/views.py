from django.contrib.auth import get_user_model
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from account.models import SocialLinks
from account.permissions import IsOwner
from account.serializers import UserListSerializer, UserRegisterSerializer, UserUpdateSerializer, SocialLinkSerializer, \
    UserDetailSerializer

User = get_user_model()


class UserModelViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'register':
            return UserRegisterSerializer
        elif self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'links':
            return SocialLinkSerializer
        return UserUpdateSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve', 'links'):
            return [IsAuthenticated()]
        elif self.action in ('update', 'partial_update'):
            return [IsOwner()]
        return [AllowAny()]

    @action(['POST'], detail=False)
    def register(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Successfully registered!', 'data': serializer.data},
                        status=201)

    from rest_framework import status

    @action(['POST'], detail=False)
    def links(self, request):
        user = request.user
        try:
            social_links = user.social
            return Response({'message': 'Already added!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SocialLinksUpdateViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [IsOwner]







