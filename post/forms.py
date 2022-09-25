from unicodedata import category
from django import forms
from .models import Post, Category
from django.core.validators import MinValueValidator, MaxValueValidator


class PostModelCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'img',
            'title',
            'description',
            'rating_stars',
            'released_date',
            'category'
        )