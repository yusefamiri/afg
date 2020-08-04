from django.views.generic import DetailView, ListView
from blog.models import Post


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = 'blog/post_list.html'
