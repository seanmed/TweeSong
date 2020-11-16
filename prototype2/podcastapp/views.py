from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    return render(request, 'podcastapp/home.html')

#def executetwitterauth(request):
    #if request.method == 'POST' and 'run_script' in request.POST:

       # from podcastapp.twitter_client import twitter_client:



            # call function
           # twitter_client()

            # return user to required page
           # return HttpResponseRedirect(reverse(app_name:view_name)
