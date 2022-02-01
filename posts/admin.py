from django.contrib import admin
from .models import Comment, Source, Author, Post

# Register your models here.
admin.site.register([Source, Comment, Author, Post])
