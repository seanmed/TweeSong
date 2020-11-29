from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='podcast_app-home'),
    path('tracks/', views.tracks, name='podcast_app-tracks')

]