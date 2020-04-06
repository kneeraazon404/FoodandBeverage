from django.shortcuts import render, redirect
from team.models import Team
import requests as req
from django.contrib.auth.decorators import login_required



def Contact(request):
    teams = Team.objects.order_by("-hire_date")
    context = {"teams": teams}
    return render(request, "contact/contact.html", context)
    


def Contribution(request):
    # import requests as req

    url ="https://uat.esewa.com.np/epay/main"
    d = {'amt': 100,
    'pdc': 0,
    'psc': 0,
    'txAmt': 0,
    'tAmt': 100,
    'pid':'ee2c3ca1-696b-4cc5-a6be-2c40d929d453',
    'scd':'epay_payment',
    'su':'http://merchant.com.np/page/esewa_payment_success?q=su',
    'fu':'http://merchant.com.np/page/esewa_payment_failed?q=fu'}
    resp = req.post(url, d)
    context={"resp":resp}
    return render(request, "contact/contribution.html", context)
