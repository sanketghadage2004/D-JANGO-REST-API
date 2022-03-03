from dataclasses import fields
from rest_framework import serializers
from .models import Blog
class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()
    
class ViewSetModel(serializers.ModelSerializer):
    class meta:
        fields=['__all__']
