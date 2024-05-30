from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = UserProfileSerializer(profile)
    return Response(serialized_profile.data)


@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = UserProfile.objects.create(
        username = request.data['username'],
    )   
    user.set_password(request.data['password'])
    user.save()
    profile = UserProfile.objects.create(
        user = user,
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
    )
    profile.save()
    profile_serialized = UserProfileSerializer(profile)
    return Response(profile_serialized.data)

@permission_classes([IsAuthenticated])  
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@permission_classes([IsAuthenticated])
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@permission_classes([IsAuthenticated])
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

@permission_classes([IsAuthenticated])
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer