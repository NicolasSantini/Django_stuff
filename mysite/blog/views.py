from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from mysite.blog.forms import PostForm, CommentForm
from mysite.blog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForms, CommentForms
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(TemplateView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')  # returns the post con data <= della data attuale in ordine cronologico (decrescente)


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    Form_class = PostForm

    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    Form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    get_queryset = Post.objects.filter(published_date__isnull = True).order_by('-created_date')


###############
#COMMENTS PART#
###############
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

