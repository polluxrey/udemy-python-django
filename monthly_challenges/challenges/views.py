from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "🍐 Partridge in a Pear Tree – Eat one nourishing meal.",
    "february": "🕊️ Two Turtle Doves – Connect with two people.",
    "march": "🐔 Three French Hens – Enjoy something cultural (music, food, film).",
    "april": "🐦 Four Calling Birds – Express yourself (write, speak, post).",
    "may": "💍 Five Golden Rings – List five things you're grateful for.",
    "june": "🥚 Six Geese A-Laying – Create something (art, food, playlist).",
    "july": "🦢 Seven Swans A-Swimming – Move your body (walk, dance, stretch).",
    "august": "🥛 Eight Maids A-Milking – Help someone in a small way.",
    "september": "💃 Nine Ladies Dancing – Do something that brings pure joy.",
    "october": "🕴 Ten Lords A-Leaping – Take a small leap outside your comfort zone.",
    "november": "🎶 Eleven Pipers Piping – Listen to something inspiring.",
    "december": "🥁 Twelve Drummers Drumming – Celebrate your progress!"
}


def monthly_challenge_by_number(request, month):
    challenge_text = None

    month_list = list(monthly_challenges.keys())

    if 1 <= month and month <= len(month_list):
        month_name = month_list[month - 1]
        redirect_path = reverse("month-challenge", args=[month_name])
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    challenge_text = None

    if month in monthly_challenges:
        challenge_text = f"{month.capitalize()}: {monthly_challenges.get(month)}"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
