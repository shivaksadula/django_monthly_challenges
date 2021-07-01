from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk at least 20min every day",
    "march": "Work hard",
    "april": "exercise",
    "may": "meet deadlines",
    "june": "take vacation",
    "july": "boat ride",
    "august": "make a new habit",
    "september": "learn new technology",
    "october": "make a diet plan",
    "november": "shopping",
    "december": "go to India",
}


def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported<h1>')
