from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id','author_username','message']