from django.shortcuts import render
from team.models import Team
from posts.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by("-post_date")[:3]
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def about(request):
    teams = Team.objects.order_by("-hire_date")
    context = {"teams": teams}
    return render(request, "blog/about.html", context)

