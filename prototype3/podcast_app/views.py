from django.shortcuts import render
from django.http import HttpResponse
import requests
from podcast_app.API_Twitter_Spotify import twitterapi
from .models import TwitterUser, Track


# Create your views here.

def home(request):


    return render(request, 'podcast_app/home.html')

def tracks(request):
    data= twitterapi()
  #  for key in data:
     #   TwitterUser.objects.create(twitter_user=key)
     #   for url in data[key]:
        #    TwitterUser.objects.get(twitter_user=key).track_set.create(track=url)

    return render(request, 'podcast_app/output.html', {'data': data.items()})
