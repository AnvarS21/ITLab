from rest_framework import serializers

from account.serializers import UserListSerializer, UserDetailSerializer
from project.models import Project, ProjectSImage, Developer


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('preview',)


class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSImage
        fields = ('image',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    images = ProjectImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        exclude = ('preview',)


class DeveloperListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)

    class Meta:
        model = Developer
        fields = ('user',)


class DeveloperDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Developer
        fields = ('user',)




