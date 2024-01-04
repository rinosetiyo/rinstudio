from django.contrib import admin
from comments.models import Comment, Reply

# Register your models here.
admin.site.register(Comment)
admin.site.register(Reply)