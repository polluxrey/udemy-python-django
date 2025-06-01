from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

month_list = ["january", "february", "march",
              "april", "may", "june", "july", "august", "september", "october", "november", "december"]


def monthly_challenge(request, month):
    challenge_text = None

    if month in month_list:
        challenge_text = f"This is for the {month.capitalize()} Challenge page!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
