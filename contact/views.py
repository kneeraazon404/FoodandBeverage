from django.shortcuts import render, redirect
from .models import Contact
import requests as req
from django.contrib import messages
from django.core.mail import send_mail
from team.models import Team

# Create your views here.


def ContactForm(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id", 1)
        post = request.POST.get("post", "")

        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                post_id=post_id, user_id=user_id
            )
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this post"
                )
                return redirect("/contact/contact")

        contact = Contact(
            post=post,
            post_id=post_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )

        contact.save()

        # Send email
        # send_mail(
        #     "Recipe post Inquiry",
        #     "There has been an inquiry for "
        #     + post
        #     + ". Sign into the admin panel for more info",
        #     "thisismyfakeacount2020@gmail.com",
        #     ["kneeraazon@gmail.com", "karkinriajan1999@gmail.com"],
        #     fail_silently=False,
        # )

        messages.success(
            request,
            "Your request has been submitted, Dilip karki will get back to you soon",
        )

        return redirect("/")
    teams = Team.objects.order_by("-hire_date")
    context = {"teams": teams}

    return render(request, "contact/contact.html", context)
