
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


def posts(request):
    postss = Post.objects.order_by("-post_date")
    paginator = Paginator(postss, 3)
    page_number = request.GET.get("page")
    paged_posts = paginator.get_page(page_number)
    context = {"posts": paged_posts}
    return render(request, "posts/posts.html", context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "posts/post.html", context)


def search(request):
    return render(request, "posts/search.html")
