from django.shortcuts import render
from django.views import generic
from .models import New


class NewsListView(generic.ListView):
    template_name = 'news/news-list.html'
    queryset = New.objects.all()
    context_object_name = 'news'

class NewsDetailView(generic.DetailView):
    template_name = 'news/news-detail.html'
    queryset = New.objects.all()
    context_object_name = 'new'