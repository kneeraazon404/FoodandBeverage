from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
import request
import re
from django import template
from django.conf import settings

register = template.Library()

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


@register.filter(name="youtube_embed_url")
# converts youtube URL into embed HTML
# value is url
def youtube_embed_url(value):
    match = re.search(
        r"^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$", value
    )
    if match:
        embed_url = "http://www.youtube.com/embed/%s" % (match.group(2))
        res = (
            '<iframe width="560" height="315" src="%s" frameborder="0" allowfullscreen></iframe>'
            % (embed_url)
        )
        return res
    return ""


youtube_embed_url.is_safe = True


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "posts/post.html", context)


def search(request):
    return render(request, "posts/search.html")
