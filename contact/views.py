from django.shortcuts import render
from team.models import Team


def Contact(request):
    teams = Team.objects.order_by("-hire_date")
    context = {"teams": teams}
    return render(request, "contact/contact.html", context)
