import stripe  # new
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render  # new


# stripe.api_key = settings.STRIPE_SECRET_KEY  # new


class HomePageView(TemplateView):
    template_name = "payments/payments.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def payments(request):
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
    return render(request, "contact/payments.html", context)
    # return render(request, "contact/payments.html", context)


@login_required()
def stripe(request):
    template_name = "payments.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
