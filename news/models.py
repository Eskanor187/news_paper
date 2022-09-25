from django.db import models
from post.models import Category
from ckeditor.fields import RichTextField


class New(models.Model):
    img = models.ImageField(upload_to='PROJECT_FOR_THE_LESSON/image', verbose_name='PhotoN', blank=True)
    title = models.CharField(max_length=40)
    preview_info = RichTextField()
    information = RichTextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)