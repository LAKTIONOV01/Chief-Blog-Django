from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment, Articles
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.

def custom_404_view(request, exception):
    return render(request, 'exception/404.html', status=404)


class HomeView(ListView):
    model = Post
    paginate_by = 7
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    extra_context = {
        'articles': Articles.objects.all(),
    }


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug'))


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        current_post = self.object
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['previous_post'] = Post.objects.filter(id__lt=current_post.id).order_by('-id').first()
        context['next_post'] = Post.objects.filter(id__gt=current_post.id).order_by('id').first()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)
