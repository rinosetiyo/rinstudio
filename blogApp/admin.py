from django.contrib import admin
from blogApp.models import Category, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)