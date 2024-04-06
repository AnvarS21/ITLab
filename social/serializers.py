from rest_framework import serializers

from social.models import News, NewsImage, AboutUs, AboutUsImages


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('speaker', 'title', 'created_at', 'preview')


class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ('image', 'title')


class NewsDetailSerializer(serializers.ModelSerializer):
    images = NewsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class AboutUsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImages
        fields = ['images']


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = ['body', 'images']