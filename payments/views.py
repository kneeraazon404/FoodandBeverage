from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



class HomePageView(TemplateView):
    template_name = "payments/payments.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context


@login_required()
def payments(request):
    return HttpResponse("Payment processing is not configured.", status=503)
