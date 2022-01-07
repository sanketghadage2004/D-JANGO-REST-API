from rest_framework import serializers

class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()
    