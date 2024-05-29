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
    class meta:
        author = AuthorSerializer()
        genre = GenreSerializer(many=True)
    class meta:
        model = Book
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = '__all__'
