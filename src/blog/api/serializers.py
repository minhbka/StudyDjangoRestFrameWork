from rest_framework import serializers
from blog.models import BlogPost


class SnippetSerializer(serializers.Serializer):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'date_updated']