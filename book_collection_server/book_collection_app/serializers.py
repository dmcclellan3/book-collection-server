from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        author = AuthorSerializer()
        genre = GenreSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
