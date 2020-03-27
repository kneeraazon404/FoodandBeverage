from django.shortcuts import render


def contact(request):
    # if request.method==POST:

    return render(request, "contact/contact.html")
