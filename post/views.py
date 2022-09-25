from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PostModelCreateForm
from .models import Post


class PostListView(generic.ListView):

    template_name ='post/post-list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):

    template_name = 'post/post-detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class PostCreateView(generic.CreateView):
    template_name = 'post/post-create.html'
    form_class = PostModelCreateForm

    def get_success_url(self):
        return reverse('post:post_list')
    
class LandingPage(generic.TemplateView):
    template_name = 'landing-page.html'

def Create(request):
    if request.method == 'POST':
        create = Post()

        create.title = request.POST.get('title')
        create.rating_stars = request.POST.get('rating_stars')
        create.description = request.POST.get('description')
        create.released_date = request.POST.get('released_date')
        create.category = request.POST.get('category')
        create.category = request.POST.get('trailer_pattern')

        if len(request.FILES) != 0:
            create.img = request.FILES['img']
        create.save()
        return redirect('posts:post_list')
    return render(request , 'post/post-create.html')