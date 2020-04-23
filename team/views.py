from django.shortcuts import render


def team(request):
    return render(request, "team/teams.html")
