from django.db import models
from django.contrib.auth.models import User
from blogApp.models import Post
from ckeditor.fields import RichTextField

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='post')
    message = RichTextField()

    def __str__(self):
        return self.message
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, related_name='reply')
    replies = RichTextField()

    def __str__(self):
        return self.replies