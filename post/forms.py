from unicodedata import category
from django import forms
from .models import Post, Category
from django.core.validators import MinValueValidator, MaxValueValidator