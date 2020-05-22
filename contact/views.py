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
                return redirect("/posts/" + post_id)

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
        send_mail(
            "Recipe post Inquiry",
            "There has been an inquiry for "
            + post
            + ". Sign into the admin panel for more info",
            "ramechhaponlinemedia@gmail.com",
            ["karkinirajan1999@gmail.com"],
            fail_silently=False,
        )

        messages.success(
            request,
            "Your request has been submitted, Dilip karki will get back to you soon",
        )

        return redirect("/")
    teams = Team.objects.order_by("-hire_date")
    context = {"teams": teams}

    return render(request, "contact/contact.html", context)


from django.conf import settings  # new
from django.views.generic.base import TemplateView


from django.conf import settings  # new
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def Contribution(request):
    # import requests as req

    url = "https://uat.esewa.com.np/epay/main"
    d = {
        "amt": 100,
        "pdc": 0,
        "psc": 0,
        "txAmt": 0,
        "tAmt": 100,
        "pid": "ee2c3ca1-696b-4cc5-a6be-2c40d929d453",
        "scd": "epay_payment",
        "su": "http://merchant.com.np/page/esewa_payment_success?q=su",
        "fu": "http://merchant.com.np/page/esewa_payment_failed?q=fu",
    }
    resp = req.post(url, d)
    context = {"resp": resp}
    return render(request, "contact/contribution.html", context)
