from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)


class ProfileAdmin(admin.ModelAdmin):
     pass

admin.site.register(UserProfile, ProfileAdmin)