from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.category_name
    
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    content = RichTextField()
    post_image = models.ImageField(upload_to='post-images/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='post_category')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title