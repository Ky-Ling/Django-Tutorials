import re
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    meetups = [
        { "title": "A first meetup", "location": "New York", "slug": "a-first-meetup" },
        { "title": "The second meetup", "location": "Paris", "slug": "a-second-meetup" },
        { "title": "The third meetup", "location": "Shanghai", "slug": "a-third-meetup" }
    ]

    return render(request, "meetups/index.html", {
        "meetups": meetups
    })



def meetup_details(request, meetup_slug):
    print(meetup_slug)
    
    selected_meetup = {
        "title": "A first meetup",
        "description": "This is the first meetup"
    }

    return render(request, "meetups/meetup-details.html", {
        "meetup_title": selected_meetup["title"],
        "meetup_description": selected_meetup["description"]
    })