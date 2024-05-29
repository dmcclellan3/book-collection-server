from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre')
    summary = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        return self.title
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)

def __str__(self):
    return self.user.username


