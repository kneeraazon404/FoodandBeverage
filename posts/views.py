from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
import request

# Create your views here.


def posts(request):
    postss = Post.objects.order_by("-post_date")
    # .filter(is_published=True). can be added to
    #  disable the unpublished post we will do it later if the case arises
    paginator = Paginator(postss, 3)
    page_number = request.GET.get("page")
    paged_posts = paginator.get_page(page_number)
    context = {"posts": paged_posts}
    return render(request, "posts/posts.html", context)


def post(request, post_id):
    return render(request, "posts/post.html")


def search(request):
    return render(request, "posts/search.html")
