from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Create an App",
    "february": "Hith the gym",
    "march": "Eat healthy food",
    "april": "prepare for exam",
    "may": "enjoy",
    "june": "enjoy",
    "july": "enjoy",
    "august": "enjoy",
    "september": "enjoy",
    "october": "enjoy",
    "november": "enjoy",
    "december": "buy a blanket"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<h1><ul>{list_items}</ul></h1>"
    return HttpResponse(response_data)


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge,
            "month": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
