from rest_framework import viewsets, routers, serializers
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import Profile, ProfilePhoto


class IsProfileOwner(BasePermission):
    """
    Custom permission to only allow owners of profile to view or edit it.
    """
    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user and
            request.method in ['GET', 'PATCH'])


class IsProfilePhotoOwner(BasePermission):
    """
    Custom permission to only allow owners of profile to view or edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.profile.user == request.user


class ProfilePhotoSerializer(serializers.ModelSerializer):

    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = ProfilePhoto
        fields = ('title', 'url')


class ProfileSerializer(serializers.ModelSerializer):

    photos = ProfilePhotoSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('name', 'photos')


class ProfileViewSet(viewsets.ModelViewSet):

    model = Profile
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, IsProfileOwner)


class ProfilePhotoViewSet(viewsets.ModelViewSet):

    model = ProfilePhoto
    serializer_class = ProfilePhotoSerializer
    permission_classes = (IsAuthenticated, IsProfilePhotoOwner)


router = routers.DefaultRouter()

router.register(r'profile', ProfileViewSet)
router.register(r'photo', ProfilePhotoViewSet)
