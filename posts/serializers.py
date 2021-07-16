from rest_framework import serializers

from posts.models import Post
from categories.models import Category
from users.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'



class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        model = Category
        fields = '__all__'







