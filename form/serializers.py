from django.db.models import QuerySet
from rest_framework import serializers

from form.models import Review, Client


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Review
        exclude = ('created_at', 'updated_at')


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('updated_at',)

    # def to_representation(self, instance):
    #     serialized_data = super().to_representation(instance)
    #     user = self.context['request'].user
    #     if serialized_data['rating'] >= 4:
    #         return serialized_data
    #     elif instance.user == user and serialized_data['rating'] < 3:
    #         return serialized_data
    #     return None
class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'