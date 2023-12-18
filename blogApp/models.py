from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.category_name
    
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = RichTextField()
    post_image = models.ImageField(upload_to='post-images/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='post_category')

    def __str__(self):
        return self.title