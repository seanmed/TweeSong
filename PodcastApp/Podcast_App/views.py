from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SearchSpotifyAPIForm
import importlib
from Podcast_App.spotify_client import *
# Create your views here

spotify= SpotifyAPI(client_id, client_secret)

def contact(request):
    if request.method == 'POST':
        form = SearchSpotifyAPIForm(request.POST)
        if form.is_valid():
            twitter_username= form.cleaned_data['twitter_username']
            r=spotify.search(twitter_username, search_type="track")





        return HttpResponse(r.items())


    form= SearchSpotifyAPIForm()
    return render(request, 'form.html', {'form': form})


