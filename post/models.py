from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    img = models.ImageField(upload_to='PROJECT_FOR_THE_LESSON/image/', verbose_name='PhotoP', blank=True)
    title = models.CharField(max_length=30)
    rating_stars = models.IntegerField(validators=[MinValueValidator(0) ,MaxValueValidator(5)])
    description = models.TextField()
    released_date = models.DateField()
    posted_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_pattern = models.URLField(None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post:post_detail', args=[str(self.id)])