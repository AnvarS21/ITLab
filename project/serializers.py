from rest_framework import serializers

from account.serializers import UserListSerializer, UserDetailSerializer, UserDeveloperList
from project.models import Project, ProjectSImage, Developer


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('preview',)


class DeveloperListSerializer(serializers.ModelSerializer):
    developer = UserDeveloperList(read_only=True)

    class Meta:
        model = Developer
        fields = ("__all__")


class DeveloperDetailSerializer(serializers.ModelSerializer):
    developer = UserDetailSerializer(read_only=True)

    class Meta:
        model = Developer
        fields = ('__all__')


class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSImage
        fields = ('image',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    images = ProjectImagesSerializer(many=True, read_only=True)
    developers = DeveloperDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        exclude = ('preview',)




